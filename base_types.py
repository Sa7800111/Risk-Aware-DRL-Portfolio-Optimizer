from enum import IntEnum, unique
from typing import TypedDict, Optional, List, Dict
import numpy as np

@unique
class Side(IntEnum):
    BUY = 1
    SELL = -1

@unique
class OrderType(IntEnum):
    LIMIT = 1
    MARKET = 2
    FOK = 3
    IOC = 4

class TradeRecord(TypedDict):
    trade_id: int
    timestamp: int
    price: float
    quantity: int
    taker_id: str
    maker_id: str
    side: int

class BookSnapshot(TypedDict):
    timestamp: int
    symbol: str
    bids: List[List[float]]
    asks: List[List[float]]