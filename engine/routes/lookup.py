from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.schemas import Creator, Email, LookupRequest
from services.youtube import get_channel_info
from services.email_finder import find_emails_for_channel

router = APIRouter()


def save_creator(db: Session, channel_info: dict) -> Creator:
    existing = db.query(Creator).filter(Creator.youtube_channel_id == channel_info["youtube_channel_id"]).first()
    if existing:
        existing.name = channel_info["name"]
        existing.description = channel_info["description"]
        existing.thumbnail_url = channel_info["thumbnail_url"]
        existing.subscriber_count = channel_info["subscriber_count"]
        existing.video_count = channel_info["video_count"]
        existing.country = channel_info["country"]
        existing.social_links = channel_info["social_links"]
        existing.category_id = channel_info.get("category_id")
        existing.tags = channel_info.get("tags", [])
        db.commit()
        db.refresh(existing)
        return existing

    creator = Creator(**channel_info)
    db.add(creator)
    db.commit()
    db.refresh(creator)
    return creator


def save_emails(db: Session, creator: Creator, emails_data: list[dict]):
    db.query(Email).filter(Email.creator_id == creator.id).delete()
    for ed in emails_data:
        email = Email(creator_id=creator.id, **ed)
        db.add(email)
    db.commit()


@router.post("/lookup")
def lookup_creator(req: LookupRequest, db: Session = Depends(get_db)):
    try:
        channel_info = get_channel_info(req.query)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"YouTube API 调用失败: {str(e)}")

    creator = save_creator(db, channel_info)

    emails_data = find_emails_for_channel(channel_info)
    save_emails(db, creator, emails_data)

    return {
        "id": str(creator.id),
        "youtube_channel_id": creator.youtube_channel_id,
        "name": creator.name,
        "description": creator.description,
        "thumbnail_url": creator.thumbnail_url,
        "subscriber_count": creator.subscriber_count,
        "video_count": creator.video_count,
        "country": creator.country,
        "emails": [{"email": e.email, "confidence_score": e.confidence_score, "source": e.source} for e in creator.emails],
    }


@router.post("/batch-lookup")
def batch_lookup(queries: list[str], db: Session = Depends(get_db)):
    results = []
    errors = []
    for q in queries:
        try:
            channel_info = get_channel_info(q)
            creator = save_creator(db, channel_info)
            emails_data = find_emails_for_channel(channel_info)
            save_emails(db, creator, emails_data)
            results.append({
                "id": str(creator.id),
                "name": creator.name,
                "thumbnail_url": creator.thumbnail_url,
                "subscriber_count": creator.subscriber_count,
                "emails": [{"email": e.email, "confidence_score": e.confidence_score} for e in creator.emails],
            })
        except Exception as e:
            errors.append({"query": q, "error": str(e)})
    return {"results": results, "errors": errors, "total": len(results)}
