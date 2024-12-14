class MarketValidator:
    def __init__(self, tick_size: float, lot_size: int):
        self.tick_size = tick_size
        self.lot_size = lot_size

    def validate_price(self, price: float) -> bool:
        if price <= 0: return False
        remainder = round(price % self.tick_size, 10)
        return remainder == 0 or remainder == self.tick_size

    def validate_quantity(self, qty: int) -> bool:
        return qty > 0 and qty % self.lot_size == 0

    def validate_order(self, order) -> bool:
        if not self.validate_price(order.price) and order.otype == OrderType.LIMIT:
            order.status = "REJECTED_INVALID_PRICE"
            return False
        if not self.validate_quantity(order.qty):
            order.status = "REJECTED_INVALID_QTY"
            return False
        return True