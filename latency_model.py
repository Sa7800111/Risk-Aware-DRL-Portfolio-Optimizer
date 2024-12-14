import numpy as np
import time

class NetworkLatency:
    def __init__(self, mean_mu: float, sigma: float):
        self.mu = mean_mu
        self.sigma = sigma

    def simulate_delay(self):
        delay = np.random.lognormal(self.mu, self.sigma)
        time.sleep(delay / 1000.0)
        return delay