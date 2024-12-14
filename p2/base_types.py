from typing import TypedDict, List, Optional
from datetime import datetime

class NewsItem(TypedDict):
    guid: str
    timestamp: datetime
    ticker: str
    headline: str
    body: str
    source: str

class EntitySignal(TypedDict):
    ticker: str
    sentiment_score: float
    relevance_score: float
    confidence: float