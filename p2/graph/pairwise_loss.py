import torch.nn as nn

class PairwiseContrastiveLoss(nn.Module):
    def __init__(self, margin: float = 1.0):
        super().__init__()
        self.margin = margin

    def forward(self, out1, out2, label):
        euclidean_dist = nn.functional.pairwise_distance(out1, out2)
        loss = torch.mean((1-label) * torch.pow(euclidean_dist, 2) +
                          (label) * torch.pow(torch.clamp(self.margin - euclidean_dist, min=0.0), 2))
        return loss