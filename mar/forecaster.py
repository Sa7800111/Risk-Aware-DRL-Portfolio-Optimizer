import numpy as np
from typing import List, Dict

class TrajectoryForecaster:
    def __init__(self, sampler: Any, horizon: int = 100):
        self.sampler = sampler
        self.horizon = horizon

    def forecast_mid_price(self, current_lob: dict, n_trajectories: int = 50) -> Dict[str, np.ndarray]:
        results = []
        for _ in range(n_trajectories):
            path = self.sampler.sample_paths(current_lob, n_paths=1, steps=self.horizon)[0]
            results.append(path)
        
        arr = np.array(results)
        return {
            "mean": np.mean(arr, axis=0),
            "upper_95": np.percentile(arr, 95, axis=0),
            "lower_05": np.percentile(arr, 5, axis=0),
            "std": np.std(arr, axis=0)
        }