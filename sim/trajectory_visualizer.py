import matplotlib.pyplot as plt

class PathVisualizer:
    def plot_trajectories(self, paths: list):
        plt.figure(figsize=(10, 6))
        for p in paths:
            plt.plot(p, alpha=0.3)
        plt.title("Market Trajectories")
        plt.show()