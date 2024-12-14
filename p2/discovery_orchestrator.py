class DiscoveryOrchestrator:
    def __init__(self, nlp_engine, graph_engine):
        self.nlp = nlp_engine
        self.graph = graph_engine

    def process_news_event(self, ticker: str, text: str):
        local_tensor = self.nlp.get_tensor(text)
        global_impact = self.graph.propagate_signal(ticker, local_tensor)
        return global_impact