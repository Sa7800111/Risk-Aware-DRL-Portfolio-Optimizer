from transformers import AutoTokenizer

class DiscoveryTokenizer:
    def __init__(self, config: DiscoveryConfig):
        self.tokenizer = AutoTokenizer.from_pretrained(config.model_name)
        self.max_len = config.max_length

    def tokenize(self, text: str):
        return self.tokenizer(
            text,
            padding="max_length",
            truncation=True,
            max_length=self.max_len,
            return_tensors="pt"
        )