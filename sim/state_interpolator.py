class StateInterpolator:
    def interpolate(self, p1: float, p2: float, steps: int):
        return list(np.linspace(p1, p2, steps))