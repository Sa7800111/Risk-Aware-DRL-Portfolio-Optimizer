import torch

class ModelCheckpoint:
    @staticmethod
    def save(model, path: str):
        torch.save(model.state_dict(), path)

    @staticmethod
    def load(model, path: str):
        model.load_state_dict(torch.load(path))