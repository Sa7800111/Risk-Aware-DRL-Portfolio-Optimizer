class MarketIntegrityMonitor:
    def detect_layering(self, order_stream: list):
        # Detection logic for spoofing/layering
        pass

    def check_circuit_breaker(self, price: float, prev_close: float):
        if abs(price - prev_close) / prev_close > 0.1:
            return "HALT"
        return "NORMAL"