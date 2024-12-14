from torch.utils.data import DataLoader

class BatchDiscoveryRunner:
    def __init__(self, inference, batch_size=32):
        self.inference = inference
        self.batch_size = batch_size

    def process_headlines(self, headlines: list):
        results = []
        for i in range(0, len(headlines), self.batch_size):
            batch = headlines[i:i + self.batch_size]
            # Parallel inference logic
            pass
        return results