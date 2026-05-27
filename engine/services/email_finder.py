import re
import httpx
from config import settings


def extract_domain_from_description(description: str, social_links: dict) -> str | None:
    """从频道描述和社交链接中提取域名"""
    text = description or ""
    for url in social_links.get("featured_channels", []):
        text += " " + url

    domain_pattern = r"(?:https?://)?(?:www\.)?([a-zA-Z0-9][a-zA-Z0-9-]*\.[a-zA-Z]{2,})"
    matches = re.findall(domain_pattern, text)
    exclude = {"youtube.com", "youtu.be", "twitter.com", "facebook.com", "instagram.com", "tiktok.com"}
    for domain in matches:
        if domain.lower() not in exclude:
            return domain.lower()
    return None


def find_emails_by_domain(domain: str) -> list[dict]:
    """通过 Hunter.io API 查找域名下的邮箱"""
    if not settings.hunter_api_key:
        return []

    try:
        response = httpx.get(
            "https://api.hunter.io/v2/domain-search",
            params={"domain": domain, "api_key": settings.hunter_api_key},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()

        emails = []
        for email_data in data.get("data", {}).get("emails", []):
            emails.append({
                "email": email_data.get("value", ""),
                "confidence_score": email_data.get("confidence", 0) / 100.0,
                "source": "hunter.io",
            })
        return emails
    except Exception:
        return []


def find_emails_for_channel(channel_info: dict) -> list[dict]:
    """为频道查找所有可能的工作邮箱"""
    description = channel_info.get("description", "")
    social_links = channel_info.get("social_links", {})

    domain = extract_domain_from_description(description, social_links)
    if domain:
        return find_emails_by_domain(domain)

    name = channel_info.get("name", "")
    if name and settings.hunter_api_key:
        try:
            response = httpx.get(
                "https://api.hunter.io/v2/email-finder",
                params={"company": name, "api_key": settings.hunter_api_key},
                timeout=10,
            )
            response.raise_for_status()
            data = response.json()
            if data.get("data", {}).get("email"):
                return [{
                    "email": data["data"]["email"],
                    "confidence_score": data["data"].get("score", 50) / 100.0,
                    "source": "hunter.io",
                }]
        except Exception:
            pass

    return []
