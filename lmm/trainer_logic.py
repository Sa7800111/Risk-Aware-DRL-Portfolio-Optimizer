class LMMTrainer:
    def __init__(self, model, lr: float = 1e-4):
        self.model = model
        self.optimizer = torch.optim.AdamW(model.parameters(), lr=lr)

    def step(self, batch_x, batch_types, batch_y):
        self.optimizer.zero_grad()
        logits = self.model(batch_x, batch_types)
        loss = F.cross_entropy(logits.view(-1, logits.size(-1)), batch_y.view(-1))
        loss.backward()
        self.optimizer.step()
        return loss.item()