class Ticker:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.open = 0.0
        self.high = 0.0
        self.low = 0.0
        self.close = 0.0
        self.volume = 0
        self.trades = []

    def update(self, price: float, qty: int):
        if self.open == 0: self.open = price
        self.high = max(self.high, price)
        self.low = min(self.low, price) if self.low > 0 else price
        self.close = price
        self.volume += qty