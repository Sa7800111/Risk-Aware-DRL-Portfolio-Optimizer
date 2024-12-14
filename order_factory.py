import time
from .base_types import Side, OrderType
from .order import Order

class OrderFactory:
    def __init__(self, default_client_id: str = "GENERIC_AGENT"):
        self.default_id = default_client_id

    def limit_buy(self, price: float, qty: int, cid: str = None) -> Order:
        return Order(cid or self.default_id, Side.BUY, price, qty, OrderType.LIMIT)

    def limit_sell(self, price: float, qty: int, cid: str = None) -> Order:
        return Order(cid or self.default_id, Side.SELL, price, qty, OrderType.LIMIT)

    def market_buy(self, qty: int, cid: str = None) -> Order:
        return Order(cid or self.default_id, Side.BUY, 0.0, qty, OrderType.MARKET)

    def market_sell(self, qty: int, cid: str = None) -> Order:
        return Order(cid or self.default_id, Side.SELL, 0.0, qty, OrderType.MARKET)

    def create_from_dict(self, d: dict) -> Order:
        try:
            return Order(
                client_id=d.get("cid", self.default_id),
                side=Side(d["side"]),
                price=float(d.get("price", 0.0)),
                qty=int(d["qty"]),
                otype=OrderType(d.get("type", 1))
            )
        except (KeyError, ValueError) as e:
            raise ValueError(f"Order creation failed: {e}")