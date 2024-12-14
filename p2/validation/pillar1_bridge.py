class MarsBridge:
    def __init__(self, mars_engine):
        self.mars = mars_engine

    def inject_discovery_signal(self, ticker, signal_vector):
        self.mars.apply_exogenous_shock(ticker, signal_vector)