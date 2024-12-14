class TemporalMarketGraph:
    def __init__(self):
        self.snapshots = []

    def add_snapshot(self, matrix: np.ndarray):
        self.snapshots.append(matrix)
        if len(self.snapshots) > 100: self.snapshots.pop(0)