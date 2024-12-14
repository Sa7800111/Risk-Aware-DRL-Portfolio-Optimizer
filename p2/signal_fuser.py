class SignalFuser:
    def fuse(self, local_signal: float, neighbor_signals: list, weights: list):
        neighbor_impact = sum(s * w for s, w in zip(neighbor_signals, weights))
        return local_signal + neighbor_impact