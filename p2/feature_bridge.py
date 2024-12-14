class NLPFeatureBridge:
    def to_tensor(self, features: dict):
        return np.array(list(features.values()), dtype=np.float32)