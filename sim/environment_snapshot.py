class EnvSnapshot:
    def __init__(self, timestamp: int, ticker: str, mid: float, spread: float, volume: int):
        self.ts = timestamp
        self.ticker = ticker
        self.mid = mid
        self.spread = spread
        self.volume = volume

    def to_vector(self):
        return [self.mid, self.spread, self.volume]