import time

class HealthMonitor:
    def log_latency(self, start_time):
        end_time = time.time()
        print(f"Discovery Latency: {end_time - start_time:.4f}s")