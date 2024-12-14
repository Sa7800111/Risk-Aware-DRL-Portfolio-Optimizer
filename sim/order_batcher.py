class OrderBatcher:
    def __init__(self, batch_size: int = 64):
        self.batch_size = batch_size
        self.current_batch = []

    def collect(self, order):
        self.current_batch.append(order)
        if len(self.current_batch) >= self.batch_size:
            batch = self.current_batch
            self.current_batch = []
            return batch
        return None