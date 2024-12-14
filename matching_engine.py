import time

class MatchingEngine:
    def __init__(self, lob: LimitOrderBook):
        self.lob = lob
        self.trades = []
        self.trade_count = 0

    def process_order(self, taker_order):
        if taker_order.otype == OrderType.MARKET:
            return self._match_market(taker_order)
        return self._match_limit(taker_order)

    def _match_limit(self, taker):
        maker_book = self.lob.asks if taker.side == Side.BUY else self.lob.bids
        
        while taker.qty > 0 and maker_book:
            best_price_key = maker_book.iloc[0]
            maker_price = -best_price_key if taker.side == Side.SELL else best_price_key
            
            if (taker.side == Side.BUY and taker.price < maker_price) or \
               (taker.side == Side.SELL and taker.price > maker_price):
                break
                
            level = maker_book[best_price_key]
            self._execute_at_level(taker, level, best_price_key, maker_book)
            
        if taker.qty > 0 and taker.otype != OrderType.IOC:
            self.lob.add_order(taker)

    def _match_market(self, taker):
        maker_book = self.lob.asks if taker.side == Side.BUY else self.lob.bids
        
        while taker.qty > 0 and maker_book:
            best_price_key = maker_book.iloc[0]
            level = maker_book[best_price_key]
            self._execute_at_level(taker, level, best_price_key, maker_book)
            
        if taker.qty > 0:
            taker.status = "CANCELLED_INSUFFICIENT_LIQUIDITY"

    def _execute_at_level(self, taker, level, price_key, book):
        while taker.qty > 0 and level:
            maker = level[0]
            trade_qty = min(taker.qty, maker.qty)
            
            maker_price = -price_key if taker.side == Side.SELL else price_key
            self.trade_count += 1
            self.trades.append({
                "tid": self.trade_count,
                "ts": time.time_ns(),
                "p": maker_price,
                "q": trade_qty,
                "taker": taker.cid,
                "maker": maker.cid,
                "side": taker.side
            })
            
            taker.fill(trade_qty)
            maker.fill(trade_qty)
            
            if maker.qty == 0:
                level.popleft()
                self.lob.remove_order(maker.oid)
                
        if not level:
            del book[price_key]