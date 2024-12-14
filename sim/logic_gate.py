class SimulationGate:
    def __init__(self, mode: str = "REALISTIC"):
        self.mode = mode

    def filter_order(self, order):
        if self.mode == "STRESS_TEST":
            return True
        return order.price > 0