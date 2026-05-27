import re
import redis
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from config import settings

cache = redis.from_url(settings.redis_url, decode_responses=True)


def extract_channel_id(query: str) -> str | None:
    """从 YouTube URL 或 @handle 中提取频道 ID"""
    patterns = [
        r"youtube\.com/channel/(UC[\w-]{22})",
        r"youtube\.com/@([\w.-]+)",
        r"youtube\.com/c/([\w.-]+)",
        r"youtube\.com/user/([\w.-]+)",
    ]
    for pattern in patterns:
        match = re.search(pattern, query)
        if match:
            return match.group(1)
    if re.match(r"^UC[\w-]{22}$", query):
        return query
    return None


def get_channel_info(query: str) -> dict:
    """获取 YouTube 频道完整信息，结果缓存 1 小时"""
    cache_key = f"yt_channel:{query}"
    cached = cache.get(cache_key)
    if cached:
        import json
        return json.loads(cached)

    youtube = build("youtube", "v3", developerKey=settings.youtube_api_key)
    channel_id = extract_channel_id(query)

    if channel_id and channel_id.startswith("UC"):
        request = youtube.channels().list(
            part="snippet,statistics,brandingSettings,topicDetails",
            id=channel_id
        )
    else:
        handle = channel_id or query.lstrip("@")
        request = youtube.channels().list(
            part="snippet,statistics,brandingSettings,topicDetails",
            forHandle=handle
        )
        try:
            resp = request.execute()
        except HttpError:
            resp = None

        if not resp or not resp.get("items"):
            request = youtube.search().list(
                part="snippet", q=query, type="channel", maxResults=1
            )
            search_resp = request.execute()
            if search_resp.get("items"):
                channel_id = search_resp["items"][0]["snippet"]["channelId"]
                request = youtube.channels().list(
                    part="snippet,statistics,brandingSettings,topicDetails",
                    id=channel_id
                )
            else:
                raise ValueError(f"未找到频道: {query}")

    response = request.execute()
    if not response.get("items"):
        raise ValueError(f"未找到频道: {query}")

    channel = response["items"][0]
    snippet = channel.get("snippet", {})
    statistics = channel.get("statistics", {})
    branding = channel.get("brandingSettings", {})
    channel_data = channel.get("topicDetails", {})

    result = {
        "youtube_channel_id": channel["id"],
        "name": snippet.get("title", ""),
        "description": snippet.get("description", ""),
        "thumbnail_url": snippet.get("thumbnails", {}).get("high", {}).get("url", ""),
        "subscriber_count": int(statistics.get("subscriberCount", 0)),
        "video_count": int(statistics.get("videoCount", 0)),
        "country": snippet.get("country", ""),
        "social_links": _extract_social_links(branding),
        "category_id": channel_data.get("topicCategories", [None])[0] if channel_data.get("topicCategories") else None,
        "tags": channel_data.get("topicCategories", []),
    }

    import json
    cache.setex(cache_key, 3600, json.dumps(result))
    return result


def _extract_social_links(branding: dict) -> dict:
    """从品牌设置中提取社交链接"""
    links = {}
    channel_branding = branding.get("channel", {})
    if channel_branding.get("featuredChannelsUrls"):
        links["featured_channels"] = channel_branding["featuredChannelsUrls"]
    if channel_branding.get("featuredChannelsTitle"):
        links["featured_titles"] = channel_branding["featuredChannelsTitle"]
    return links


def get_channel_videos(channel_id: str, max_results: int = 50) -> list[dict]:
    """获取频道的视频列表（标题、描述、标签）"""
    cache_key = f"yt_videos:{channel_id}:{max_results}"
    cached = cache.get(cache_key)
    if cached:
        import json
        return json.loads(cached)

    youtube = build("youtube", "v3", developerKey=settings.youtube_api_key)

    channel_resp = youtube.channels().list(
        part="contentDetails", id=channel_id
    ).execute()
    if not channel_resp.get("items"):
        return []
    uploads_playlist = channel_resp["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    videos = []
    next_page_token = None
    while len(videos) < max_results:
        playlist_request = youtube.playlistItems().list(
            part="snippet",
            playlistId=uploads_playlist,
            maxResults=min(50, max_results - len(videos)),
            pageToken=next_page_token
        )
        playlist_response = playlist_request.execute()
        video_ids = [
            item["snippet"]["resourceId"]["videoId"]
            for item in playlist_response.get("items", [])
        ]

        if video_ids:
            video_request = youtube.videos().list(part="snippet", id=",".join(video_ids))
            video_response = video_request.execute()
            for video in video_response.get("items", []):
                snippet = video.get("snippet", {})
                videos.append({
                    "title": snippet.get("title", ""),
                    "description": snippet.get("description", ""),
                    "tags": snippet.get("tags", []),
                })

        next_page_token = playlist_response.get("nextPageToken")
        if not next_page_token:
            break

    import json
    cache.setex(cache_key, 3600, json.dumps(videos))
    return videos


def search_channels_by_category(category_id: str, exclude_channel_id: str, max_results: int = 50) -> list[dict]:
    """按分类搜索相关频道作为相似度候选池"""
    cache_key = f"yt_category:{category_id}:{max_results}"
    cached = cache.get(cache_key)
    if cached:
        import json
        return json.loads(cached)

    youtube = build("youtube", "v3", developerKey=settings.youtube_api_key)
    # topicId 可能为 None 或不是有效 ID，此时用搜索接口做 fallback
    try:
        request = youtube.search().list(
            part="snippet",
            topicId=category_id,
            type="channel",
            maxResults=min(50, max_results),
            order="relevance"
        )
        response = request.execute()
    except HttpError:
        return []

    channels = []
    for item in response.get("items", []):
        channel_id = item["snippet"]["channelId"]
        if channel_id == exclude_channel_id:
            continue
        channels.append({
            "channel_id": channel_id,
            "name": item["snippet"]["title"],
            "description": item["snippet"]["description"],
            "thumbnail_url": item["snippet"]["thumbnails"].get("default", {}).get("url", ""),
        })
        if len(channels) >= max_results:
            break

    import json
    cache.setex(cache_key, 3600, json.dumps(channels))
    return channels
