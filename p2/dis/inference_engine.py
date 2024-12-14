import torch

class DiscoveryInference:
    def __init__(self, model, tokenizer, device):
        self.model = model.to(device)
        self.tokenizer = tokenizer
        self.device = device
        self.model.eval()

    @torch.no_grad()
    def get_tensor(self, text: str):
        inputs = self.tokenizer.tokenize(text).to(self.device)
        output = self.model(inputs['input_ids'], inputs['attention_mask'])
        return output.squeeze()