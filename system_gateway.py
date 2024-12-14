class MarsGateway:
    def __init__(self, tickers: list):
        self.state = ExchangeState(tickers)
        self.logger = AuditLogger("logs/audit")
        self.pub = MarketDataPublisher()
        self.perf = PerformanceTracker()

    def handle_request(self, ticker: str, order_data: dict):
        start = time.time_ns()
        order = OrderFactory().create_from_dict(order_data)
        success = self.state.submit(ticker, order)
        if success:
            self.perf.record_latency(start)
            depth = self.state.books[ticker].get_depth(5)
            self.pub.publish_update(ticker, depth)
            return True
        return False