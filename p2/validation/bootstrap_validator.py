class BootstrapValidator:
    def run(self, data, func, n_iterations=1000):
        stats = []
        for _ in range(n_iterations):
            sample = data.sample(frac=1.0, replace=True)
            stats.append(func(sample))
        return np.percentile(stats, [2.5, 97.5])