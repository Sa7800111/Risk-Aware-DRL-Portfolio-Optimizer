from core.clearing import ClearingHouse

class InteractiveClearing(ClearingHouse):
    def __init__(self):
        super().__init__()
        self.pending_settlements = []

    def queue_settlement(self, trade: dict):
        self.pending_settlements.append(trade)

    def finalize_batch(self):
        for trade in self.pending_settlements:
            self.process_trade(trade)
        self.pending_settlements = []