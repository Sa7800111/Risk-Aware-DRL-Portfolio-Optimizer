import torch
import lz4.frame

class TensorExporter:
    def serialize_to_binary(self, tensor: torch.Tensor, path: str):
        data = tensor.numpy().tobytes()
        compressed = lz4.frame.compress(data)
        with open(path, 'wb') as f:
            f.write(compressed)