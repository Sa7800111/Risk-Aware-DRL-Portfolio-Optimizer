class TopologyMonitor:
    def check_stability(self, m1: np.ndarray, m2: np.ndarray):
        return np.linalg.norm(m1 - m2)