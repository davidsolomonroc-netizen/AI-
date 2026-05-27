CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE creators (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    youtube_channel_id VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(500) NOT NULL,
    description TEXT,
    thumbnail_url VARCHAR(1000),
    subscriber_count BIGINT DEFAULT 0,
    video_count BIGINT DEFAULT 0,
    country VARCHAR(10),
    social_links JSONB DEFAULT '{}',
    category_id VARCHAR(50),
    tags JSONB DEFAULT '[]',
    last_updated TIMESTAMP DEFAULT NOW(),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE emails (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    creator_id UUID REFERENCES creators(id) ON DELETE CASCADE,
    email VARCHAR(500) NOT NULL,
    confidence_score FLOAT DEFAULT 0,
    source VARCHAR(100),
    verified_at TIMESTAMP DEFAULT NOW(),
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(creator_id, email)
);

CREATE TABLE searches (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    query VARCHAR(500) NOT NULL,
    results JSONB DEFAULT '[]',
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE similarity_cache (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    source_creator_id UUID REFERENCES creators(id) ON DELETE CASCADE,
    target_creator_id UUID REFERENCES creators(id) ON DELETE CASCADE,
    score FLOAT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_creators_channel_id ON creators(youtube_channel_id);
CREATE INDEX idx_emails_creator_id ON emails(creator_id);
CREATE UNIQUE INDEX idx_similarity_pair ON similarity_cache(source_creator_id, target_creator_id);
CREATE INDEX idx_similarity_created ON similarity_cache(created_at);
CREATE INDEX idx_searches_created ON searches(created_at);
