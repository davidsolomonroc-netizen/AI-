export interface CreatorEmail {
  email: string;
  confidence_score: number;
  source: string | null;
}

export interface Creator {
  id: string;
  youtube_channel_id: string;
  name: string;
  description: string | null;
  thumbnail_url: string | null;
  subscriber_count: number;
  video_count: number;
  country: string | null;
  emails: CreatorEmail[];
}

export interface SimilarCreator {
  id: string;
  name: string;
  thumbnail_url: string | null;
  subscriber_count: number;
  similarity_score: number;
}

export interface LookupResponse {
  id: string;
  youtube_channel_id: string;
  name: string;
  description: string | null;
  thumbnail_url: string | null;
  subscriber_count: number;
  video_count: number;
  country: string | null;
  emails: CreatorEmail[];
}

export interface SimilarResponse {
  creators: SimilarCreator[];
  cached: boolean;
}
