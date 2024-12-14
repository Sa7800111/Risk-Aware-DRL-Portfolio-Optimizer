import time

class SimulationClock:
    def __init__(self, speed_factor: float = 1.0):
        self.start_wall = time.time_ns()
        self.start_sim = 0
        self.factor = speed_factor

    def get_sim_time(self) -> int:
        elapsed = time.time_ns() - self.start_wall
        return int(self.start_sim + (elapsed * self.factor))