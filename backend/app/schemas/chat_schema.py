from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    user_id: str
    query: str

class SourceMetadata(BaseModel):
    doc_id: str
    page: str
    score: float

class ChatResponse(BaseModel):
    answer: str
    sources: List[SourceMetadata]
    confidence: float
