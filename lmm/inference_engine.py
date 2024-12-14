class LMMInference:
    def __init__(self, model, device='cpu'):
        self.model = model.to(device)
        self.device = device

    @torch.no_grad()
    def generate_next(self, tokens, types, temp: float = 1.0):
        logits = self.model(tokens.to(self.device), types.to(self.device))
        probs = F.softmax(logits[:, -1, :] / temp, dim=-1)
        return torch.multinomial(probs, 1)