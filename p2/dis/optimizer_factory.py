from torch.optim import AdamW

class DiscoveryOptimizer:
    @staticmethod
    def get_optimizer(model, lr=2e-5, weight_decay=0.01):
        return AdamW(model.parameters(), lr=lr, weight_decay=weight_decay)