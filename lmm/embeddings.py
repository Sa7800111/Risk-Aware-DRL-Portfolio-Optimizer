import torch
import torch.nn as nn

class MarketEmbedding(nn.Module):
    def __init__(self, vocab_size: int, d_model: int, max_seq: int = 1024):
        super().__init__()
        self.tok_emb = nn.Embedding(vocab_size, d_model)
        self.pos_emb = nn.Parameter(torch.zeros(1, max_seq, d_model))
        self.type_emb = nn.Embedding(3, d_model)
        self.drop = nn.Dropout(0.1)

    def forward(self, x, types):
        b, t = x.size()
        x = self.tok_emb(x) + self.pos_emb[:, :t, :] + self.type_emb(types)
        return self.drop(x)