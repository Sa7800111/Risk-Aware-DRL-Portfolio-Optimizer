from scipy.stats import norm

class DMTest:
    def __init__(self, crit_val: float = 1.96):
        self.crit_val = crit_val

    def compare_forecasts(self, actual, pred1, pred2, h=1):
        e1 = (actual - pred1)**2
        e2 = (actual - pred2)**2
        d = e1 - e2
        d_mean = np.mean(d)
        
        gamma = np.zeros(h)
        for i in range(h):
            gamma[i] = np.mean((d[i:] - d_mean) * (d[:len(d)-i] - d_mean))
        
        var_d = (gamma[0] + 2 * np.sum(gamma[1:])) / len(d)
        dm_stat = d_mean / np.sqrt(var_d)
        p_value = 2 * (1 - norm.cdf(abs(dm_stat)))
        
        return dm_stat, p_value