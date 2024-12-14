class SimulationValidator:
    def compare_distributions(self, real_data, sim_data):
        from scipy.stats import wasserstein_distance
        return wasserstein_distance(real_data, sim_data)