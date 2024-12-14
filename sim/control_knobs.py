class ControlKnobs:
    def __init__(self):
        self.intensity = 1.0
        self.skew = 0.0
        self.granularity = "order"

    def set_knob(self, key: str, value: float):
        if hasattr(self, key):
            setattr(self, key, value)