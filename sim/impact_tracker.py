class ImpactTracker:
    def __init__(self):
        self.baseline_prices = {}
        self.impact_logs = []

    def record_pre_impact(self, ticker: str, price: float):
        self.baseline_prices[ticker] = price

    def calculate_post_impact(self, ticker: str, current_price: float):
        if ticker in self.baseline_prices:
            slippage = (current_price - self.baseline_prices[ticker]) / self.baseline_prices[ticker]
            self.impact_logs.append({"ticker": ticker, "slippage": slippage, "ts": time.time_ns()})
            return slippage
        return 0.0