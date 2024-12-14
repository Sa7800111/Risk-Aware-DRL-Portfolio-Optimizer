import torch.nn as nn

class DiscoveryModel(nn.Module):
    def __init__(self, config: DiscoveryConfig):
        super().__init__()
        self.encoder = BertSignalEncoder(config)
        self.head = FeatureExtractionHead(config)

    def forward(self, input_ids, attention_mask):
        features = self.encoder(input_ids, attention_mask)
        return self.head(features)