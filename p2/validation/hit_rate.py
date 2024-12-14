class DirectionalAccuracy:
    def compute_hit_rate(self, signals, actual_returns):
        predicted_dir = np.sign(signals)
        actual_dir = np.sign(actual_returns)
        correct = (predicted_dir == actual_dir).sum()
        return correct / len(signals)