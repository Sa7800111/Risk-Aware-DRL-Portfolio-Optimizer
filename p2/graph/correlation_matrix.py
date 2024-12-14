import numpy as np

class InteractionMatrix:
    def __init__(self, tickers: list):
        self.tickers = tickers
        self.size = len(tickers)
        self.matrix = np.eye(self.size)

    def update_correlation(self, t1: str, t2: str, value: float):
        idx1, idx2 = self.tickers.index(t1), self.tickers.index(t2)
        self.matrix[idx1, idx2] = value
        self.matrix[idx2, idx1] = value