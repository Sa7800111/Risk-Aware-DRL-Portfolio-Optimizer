import torch.nn as nn

class MultiGPUDiscovery(nn.Module):
    def __init__(self, model):
        super().__init__()
        self.model = nn.DataParallel(model)

    def forward(self, x, mask):
        return self.model(x, mask)