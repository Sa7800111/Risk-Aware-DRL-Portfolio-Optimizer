class ImpactHeatMap:
    def __init__(self, grid_size: int = 10):
        self.grid = np.zeros((grid_size, grid_size))

    def update(self, x: int, y: int, val: float):
        self.grid[x, y] += val