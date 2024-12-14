class AssetNode:
    def __init__(self, ticker: str, sector: str):
        self.ticker = ticker
        self.sector = sector
        self.adjacency_list = {}

    def add_edge(self, target_ticker: str, weight: float):
        self.adjacency_list[target_ticker] = weight