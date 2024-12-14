class LargeMarketModel(nn.Module):
    def __init__(self, vocab_size: int, d_model: int = 512, n_layers: int = 8):
        super().__init__()
        self.emb = MarketEmbedding(vocab_size, d_model)
        self.blocks = nn.ModuleList([LMMBlock(d_model, 8) for _ in range(n_layers)])
        self.ln_f = nn.LayerNorm(d_model)
        self.head = nn.Linear(d_model, vocab_size, bias=False)

    def forward(self, x, types):
        x = self.emb(x, types)
        for block in self.blocks:
            x = block(x)
        return self.head(self.ln_f(x))