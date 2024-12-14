import torch.nn as nn

class DiscoveryLoss(nn.Module):
    def __init__(self):
        super().__init__()
        self.mse = nn.MSELoss()
        self.cosine = nn.CosineEmbeddingLoss()

    def forward(self, pred, target):
        return self.mse(pred, target)