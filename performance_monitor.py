class PerformanceTracker:
    def __init__(self):
        self.latencies = []
        self.total_orders = 0

    def record_latency(self, start_ns: int):
        self.latencies.append(time.time_ns() - start_ns)
        self.total_orders += 1

    def get_stats(self):
        if not self.latencies: return {}
        return {
            "avg_latency_ns": sum(self.latencies) / len(self.latencies),
            "p99_latency_ns": sorted(self.latencies)[int(0.99 * len(self.latencies))],
            "tps": self.total_orders
        }