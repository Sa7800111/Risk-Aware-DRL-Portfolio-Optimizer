from torch.utils.data import Dataset, DataLoader

class MarketDataset(Dataset):
    def __init__(self, token_seqs, types_seqs):
        self.x = token_seqs[:-1]
        self.y = token_seqs[1:]
        self.t = types_seqs[:-1]

    def __len__(self): return len(self.x)
    def __getitem__(self, i): return self.x[i], self.t[i], self.y[i]