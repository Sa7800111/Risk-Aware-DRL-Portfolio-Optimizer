from dataclasses import dataclass

@dataclass
class DiscoveryConfig:
    model_name: str = "ProsusAI/finbert"
    max_length: int = 512
    batch_size: int = 32
    device: str = "cuda"
    output_dim: int = 7
    hidden_dim: int = 768