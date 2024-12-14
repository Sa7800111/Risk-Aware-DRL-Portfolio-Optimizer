class RiskManager:
    def __init__(self, max_order_value: float, max_position: int, price_band_pct: float = 0.1):
        self.max_order_value = max_order_value
        self.max_position = max_position
        self.price_band = price_band_pct
        self.positions = {}

    def check_order(self, order, mid_price: float) -> bool:
        if mid_price > 0:
            upper = mid_price * (1 + self.price_band)
            lower = mid_price * (1 - self.price_band)
            if order.price > upper or order.price < lower:
                return False
        
        if (order.price * order.qty) > self.max_order_value:
            return False
            
        current_pos = self.positions.get(order.cid, 0)
        new_pos = current_pos + (order.qty if order.side == Side.BUY else -order.qty)
        if abs(new_pos) > self.max_position:
            return False
            
        return True

    def update_position(self, cid: str, qty_delta: int, side: Side):
        if cid not in self.positions:
            self.positions[cid] = 0
        self.positions[cid] += (qty_delta if side == Side.BUY else -qty_delta)