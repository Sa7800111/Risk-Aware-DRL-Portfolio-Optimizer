class DiscoveryPipeline:
    def __init__(self, inference_engine, normalizer):
        self.engine = inference_engine
        self.norm = normalizer

    def run_inference(self, raw_text: str):
        tensor = self.engine.get_tensor(raw_text)
        scaled_tensor = self.norm.scale_sentiment(tensor)
        return scaled_tensor