class ScenarioEngine:
    def __init__(self, interface: MarSInterface):
        self.interface = interface
        self.templates = {
            "flash_crash": {"volatility": 0.8, "direction": -1, "intensity": 10},
            "short_squeeze": {"volatility": 0.6, "direction": 1, "intensity": 15},
            "mean_reversion": {"volatility": 0.2, "direction": 0, "intensity": 5}
        }

    def trigger_scenario(self, name: str, ticker: str):
        params = self.templates.get(name)
        if params:
            self.interface.inference.set_bias(params)
            return True
        return False