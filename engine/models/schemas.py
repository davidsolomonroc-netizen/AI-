import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, BigInteger, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from pydantic import BaseModel as PydanticBase
from database import Base


class Creator(Base):
    __tablename__ = "creators"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    youtube_channel_id = Column(String(255), unique=True, nullable=False)
    name = Column(String(500), nullable=False)
    description = Column(Text)
    thumbnail_url = Column(String(1000))
    subscriber_count = Column(BigInteger, default=0)
    video_count = Column(BigInteger, default=0)
    country = Column(String(10))
    social_links = Column(JSONB, default={})
    category_id = Column(String(50))
    tags = Column(JSONB, default=[])
    last_updated = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)

    emails = relationship("Email", back_populates="creator", cascade="all, delete-orphan")


class Email(Base):
    __tablename__ = "emails"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    creator_id = Column(UUID(as_uuid=True), ForeignKey("creators.id", ondelete="CASCADE"), nullable=False)
    email = Column(String(500), nullable=False)
    confidence_score = Column(Float, default=0)
    source = Column(String(100))
    verified_at = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)

    creator = relationship("Creator", back_populates="emails")


class SimilarityCache(Base):
    __tablename__ = "similarity_cache"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    source_creator_id = Column(UUID(as_uuid=True), ForeignKey("creators.id", ondelete="CASCADE"), nullable=False)
    target_creator_id = Column(UUID(as_uuid=True), ForeignKey("creators.id", ondelete="CASCADE"), nullable=False)
    score = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


# Pydantic request/response models
class LookupRequest(PydanticBase):
    query: str


class EmailResponse(PydanticBase):
    email: str
    confidence_score: float
    source: str | None = None


class CreatorResponse(PydanticBase):
    id: str
    youtube_channel_id: str
    name: str
    description: str | None = None
    thumbnail_url: str | None = None
    subscriber_count: int = 0
    video_count: int = 0
    country: str | None = None
    emails: list[EmailResponse] = []


class ExportRequest(PydanticBase):
    creator_ids: list[str]


class SimilarRequest(PydanticBase):
    creator_id: str


class SimilarCreatorResponse(PydanticBase):
    id: str
    name: str
    thumbnail_url: str | None = None
    subscriber_count: int = 0
    similarity_score: float
