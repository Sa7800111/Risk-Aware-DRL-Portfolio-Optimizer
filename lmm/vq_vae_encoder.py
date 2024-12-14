class OrderBatchEncoder(nn.Module):
    def __init__(self, in_channels: int = 3, latent_dim: int = 64):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(in_channels, 32, 4, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 64, 4, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, latent_dim, 3, stride=1, padding=1)
        )

    def forward(self, x):
        return self.conv(x)