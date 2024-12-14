class VectorQuantizer(nn.Module):
    def __init__(self, num_embeddings: int, embedding_dim: int):
        super().__init__()
        self.num_embeddings = num_embeddings
        self.embedding_dim = embedding_dim
        self.embedding = nn.Embedding(num_embeddings, embedding_dim)
        self.embedding.weight.data.uniform_(-1/num_embeddings, 1/num_embeddings)

    def forward(self, x):
        x_flat = x.permute(0, 2, 3, 1).reshape(-1, self.embedding_dim)
        dist = torch.cdist(x_flat, self.embedding.weight)
        indices = torch.argmin(dist, dim=1).unsqueeze(1)
        quantized = self.embedding(indices).view(x.permute(0, 2, 3, 1).shape).permute(0, 3, 1, 2)
        return quantized, indices