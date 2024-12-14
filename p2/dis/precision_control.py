import torch

class PrecisionManager:
    def __init__(self, use_fp16=True):
        self.scaler = torch.cuda.amp.GradScaler(enabled=use_fp16)

    def autocast(self):
        return torch.cuda.amp.autocast()