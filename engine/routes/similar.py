from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, UTC
from database import get_db
from models.schemas import Creator, SimilarityCache
from services.youtube import get_channel_info, search_channels_by_category
from services.similarity import find_similar_channels

router = APIRouter()


@router.post("/similar")
def find_similar(req: dict, db: Session = Depends(get_db)):
    creator_id = req.get("creator_id")
    creator = db.query(Creator).filter(Creator.id == creator_id).first()
    if not creator:
        raise HTTPException(status_code=404, detail="创作者不存在")

    cutoff = datetime.now(UTC) - timedelta(hours=24)
    cached = db.query(SimilarityCache).filter(
        SimilarityCache.source_creator_id == creator.id,
        SimilarityCache.created_at >= cutoff
    ).all()

    if cached:
        result = []
        for c in cached:
            target = db.query(Creator).filter(Creator.id == c.target_creator_id).first()
            if target:
                result.append({
                    "id": str(target.id),
                    "name": target.name,
                    "thumbnail_url": target.thumbnail_url,
                    "subscriber_count": target.subscriber_count,
                    "similarity_score": round(c.score, 4),
                })
        result.sort(key=lambda x: x["similarity_score"], reverse=True)
        return {"creators": result[:20], "cached": True}

    category_id = creator.category_id
    if not category_id:
        candidates = search_channels_by_category(
            creator.tags[0] if creator.tags else "",
            creator.youtube_channel_id,
            max_results=30
        )
    else:
        candidates = search_channels_by_category(category_id, creator.youtube_channel_id, max_results=30)

    if not candidates:
        return {"creators": [], "cached": False}

    candidate_channel_ids = [c["channel_id"] for c in candidates]

    results = find_similar_channels(creator.youtube_channel_id, candidate_channel_ids)

    response_list = []
    for channel_id, score in results:
        if score < 0.05:
            continue
        target = db.query(Creator).filter(Creator.youtube_channel_id == channel_id).first()
        if not target:
            try:
                channel_info = get_channel_info(channel_id)
                target = Creator(**channel_info)
                db.add(target)
                db.flush()
            except Exception:
                continue

        db.add(SimilarityCache(source_creator_id=creator.id, target_creator_id=target.id, score=score))
        response_list.append({
            "id": str(target.id),
            "name": target.name,
            "thumbnail_url": target.thumbnail_url,
            "subscriber_count": target.subscriber_count,
            "similarity_score": round(score, 4),
        })

    db.commit()
    response_list.sort(key=lambda x: x["similarity_score"], reverse=True)
    return {"creators": response_list[:20], "cached": False}
