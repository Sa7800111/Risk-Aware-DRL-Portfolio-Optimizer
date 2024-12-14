import torch

class DiscoveryActivations:
    def __init__(self, model):
        self.model = model
        self.activations = {}

    def hook_fn(self, name):
        def hook(model, input, output):
            self.activations[name] = output.detach()
        return hook