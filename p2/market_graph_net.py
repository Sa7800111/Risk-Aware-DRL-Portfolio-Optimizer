class MarketGraphNet(nn.Module):
    def __init__(self, n_feat, n_hid, n_class):
        super().__init__()
        self.gc1 = GraphConvLayer(n_feat, n_hid)
        self.gc2 = GraphConvLayer(n_hid, n_class)

    def forward(self, x, adj):
        x = nn.functional.relu(self.gc1(x, adj))
        return self.gc2(x, adj)