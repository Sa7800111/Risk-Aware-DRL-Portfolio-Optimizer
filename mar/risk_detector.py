class MarketRiskSystem:
    def __init__(self, threshold: float = 0.5):
        self.threshold = threshold

    def detect_volatility_collapse(self, forecasts: dict) -> bool:
        initial_var = forecasts["std"][0]
        final_var = forecasts["std"][-1]
        if final_var < initial_var * self.threshold:
            return True
        return False

    def identify_tail_risk(self, trajectories: np.ndarray, var_level: float = 0.01):
        returns = (trajectories[:, -1] - trajectories[:, 0]) / trajectories[:, 0]
        return np.percentile(returns, var_level * 100)