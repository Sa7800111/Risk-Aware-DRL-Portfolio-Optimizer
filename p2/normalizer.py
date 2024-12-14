class SignalNormalizer:
    @staticmethod
    def scale_sentiment(val: float, min_v: float = -1.0, max_v: float = 1.0):
        return (val - min_v) / (max_v - min_v)