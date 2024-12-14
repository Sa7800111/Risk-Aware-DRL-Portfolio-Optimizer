import torch

class ONNXExporter:
    @staticmethod
    def export(model, dummy_input, path):
        torch.onnx.export(model, dummy_input, path, opset_version=11)