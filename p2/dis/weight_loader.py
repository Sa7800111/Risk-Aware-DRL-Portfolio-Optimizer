import torch
import os

class ModelWeightManager:
    @staticmethod
    def save_checkpoint(model, path, epoch):
        torch.save(model.state_dict(), os.path.join(path, f"checkpoint_{epoch}.pt"))

    @staticmethod
    def load_weights(model, path):
        model.load_state_dict(torch.load(path))
        return model