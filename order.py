import time
import uuid

class Order:
    __slots__ = ['oid', 'cid', 'side', 'price', 'qty', 'initial_qty', 'otype', 'ts', 'status']
    
    def __init__(self, client_id: str, side: Side, price: float, qty: int, otype: OrderType = OrderType.LIMIT):
        if not isinstance(side, Side):
            raise ValueError("Invalid Side")
        if qty <= 0:
            raise ValueError("Quantity must be positive")
        if otype == OrderType.LIMIT and price <= 0:
            raise ValueError("Limit price must be positive")
            
        self.oid = uuid.uuid4().int
        self.cid = client_id
        self.side = side
        self.price = round(float(price), 8)
        self.qty = int(qty)
        self.initial_qty = self.qty
        self.otype = otype
        self.ts = time.time_ns()
        self.status = "NEW"

    def fill(self, fill_qty: int):
        if fill_qty > self.qty:
            raise RuntimeError("Overfill detected")
        self.qty -= fill_qty
        if self.qty == 0:
            self.status = "FILLED"
        else:
            self.status = "PARTIAL"

    def __repr__(self):
        return f"Order(id={self.oid}, side={self.side.name}, p={self.price}, q={self.qty}/{self.initial_qty})"