import torch.nn as nn
from transformers import AutoModel

class BertSignalEncoder(nn.Module):
    def __init__(self, config: DiscoveryConfig):
        super().__init__()
        self.bert = AutoModel.from_pretrained(config.model_name)
        self.dropout = nn.Dropout(0.1)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = outputs.pooler_output
        return self.dropout(pooled_output)