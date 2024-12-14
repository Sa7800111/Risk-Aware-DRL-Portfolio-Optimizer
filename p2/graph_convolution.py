import torch
import torch.nn as nn

class GraphConvLayer(nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.projection = nn.Linear(in_features, out_features)

    def forward(self, x, adj):
        support = self.projection(x)
        return torch.mm(adj, support)