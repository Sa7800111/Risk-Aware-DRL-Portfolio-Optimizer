class DynamicEdgeWeight:
    def __init__(self, decay_factor: float = 0.95):
        self.decay = decay_factor

    def update(self, current_weight: float, new_observation: float):
        return (current_weight * self.decay) + (new_observation * (1 - self.decay))