from collections import deque
from sortedcontainers import SortedDict
import numpy as np

class LimitOrderBook:
    def __init__(self, symbol: str, tick_size: float = 0.01):
        self.symbol = symbol
        self.tick_size = tick_size
        self.bids = SortedDict()
        self.asks = SortedDict()
        self.order_map = {}
        self.last_update_ts = 0

    def add_order(self, order):
        book = self.bids if order.side == Side.BUY else self.asks
        price_key = -order.price if order.side == Side.BUY else order.price
        
        if price_key not in book:
            book[price_key] = deque()
        
        book[price_key].append(order)
        self.order_map[order.oid] = order
        self.last_update_ts = order.ts

    def remove_order(self, oid: int):
        if oid not in self.order_map:
            return False
            
        order = self.order_map[oid]
        book = self.bids if order.side == Side.BUY else self.asks
        price_key = -order.price if order.side == Side.BUY else order.price
        
        if price_key in book:
            try:
                book[price_key].remove(order)
                if not book[price_key]:
                    del book[price_key]
            except ValueError:
                pass
                
        del self.order_map[oid]
        return True

    def get_mid_price(self) -> float:
        best_bid = self.get_best_bid()
        best_ask = self.get_best_ask()
        if best_bid and best_ask:
            return (best_bid + best_ask) / 2.0
        return 0.0

    def get_best_bid(self) -> float:
        return -self.bids.iloc[0] if self.bids else 0.0

    def get_best_ask(self) -> float:
        return self.asks.iloc[0] if self.asks else 0.0

    def get_depth(self, levels: int = 10):
        bids = [[-p, sum(o.qty for o in self.bids[p])] for p in self.bids.iloc[:levels]]
        asks = [[p, sum(o.qty for o in self.asks[p])] for p in self.asks.iloc[:levels]]
        return {"bids": bids, "asks": asks}