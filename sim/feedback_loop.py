class FeedbackLoop:
    def __init__(self, gateway: MarsGateway, monitor: Any):
        self.gateway = gateway
        self.monitor = monitor

    def adjust_generation_speed(self):
        tps = self.monitor.perf.get_stats().get("tps", 0)
        if tps > 5000:
            return 0.005
        return 0.001