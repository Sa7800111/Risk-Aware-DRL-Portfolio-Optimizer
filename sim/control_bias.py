import torch

class GenerationBias:
    def __init__(self, vocab_size: int):
        self.vocab_size = vocab_size
        self.bias_vector = torch.zeros(vocab_size)

    def update_bias(self, direction: int, intensity: float):
        if direction > 0:
            self.bias_vector[100:200] += intensity
        elif direction < 0:
            self.bias_vector[0:100] += intensity

    def apply(self, logits):
        return logits + self.bias_vector