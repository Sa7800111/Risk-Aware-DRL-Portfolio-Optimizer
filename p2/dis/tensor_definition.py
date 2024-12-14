class NLPTensor:
    KEYS = [
        "SENTIMENT", 
        "CONFIDENCE", 
        "RELEVANCE", 
        "URGENCY", 
        "MARKET_IMPACT", 
        "SECTOR_CORRELATION", 
        "VOLATILITY_PROXY"
    ]
    
    @staticmethod
    def to_dict(tensor_values):
        return dict(zip(NLPTensor.KEYS, tensor_values.tolist()))