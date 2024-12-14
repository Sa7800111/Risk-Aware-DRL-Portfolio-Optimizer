class ScalingMonitor:
    def __init__(self):
        self.history = []

    def log_metrics(self, params, tokens, loss):
        self.history.append({"params": params, "tokens": tokens, "loss": loss})
        print(f"P: {params} | T: {tokens} | L: {loss:.4f}")