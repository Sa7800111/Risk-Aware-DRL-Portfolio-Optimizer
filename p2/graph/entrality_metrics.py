import networkx as nx

class MarketCentrality:
    def __init__(self, matrix: np.ndarray, tickers: list):
        self.G = nx.from_numpy_array(matrix)
        self.mapping = {i: t for i, t in enumerate(tickers)}

    def get_influence_scores(self):
        scores = nx.eigenvector_centrality_numpy(self.G)
        return {self.mapping[i]: s for i, s in scores.items()}