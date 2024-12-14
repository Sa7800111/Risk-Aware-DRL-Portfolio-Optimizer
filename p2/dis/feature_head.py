import torch.nn as nn

class FeatureExtractionHead(nn.Module):
    def __init__(self, config: DiscoveryConfig):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(config.hidden_dim, 256),
            nn.ReLU(),
            nn.Linear(256, config.output_dim),
            nn.Tanh()
        )

    def forward(self, x):
        return self.fc(x)