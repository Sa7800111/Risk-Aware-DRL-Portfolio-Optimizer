class SectorExtractor:
    def get_subgraph(self, full_graph, sector_name: str):
        return {k: v for k, v in full_graph.items() if v.sector == sector_name}