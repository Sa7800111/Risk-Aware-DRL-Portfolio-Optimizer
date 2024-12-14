class RippleEffectEngine:
    def __init__(self, matrix: InteractionMatrix):
        self.matrix = matrix

    def propagate_signal(self, source_ticker: str, initial_impact: float):
        source_idx = self.matrix.tickers.index(source_ticker)
        correlations = self.matrix.matrix[source_idx]
        return correlations * initial_impact