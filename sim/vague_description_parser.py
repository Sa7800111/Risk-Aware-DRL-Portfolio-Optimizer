class PromptParser:
    def __init__(self):
        self.keyword_map = {
            "panic": {"volatility": 0.9, "direction": -1},
            "euphoria": {"volatility": 0.7, "direction": 1},
            "stability": {"volatility": 0.1, "direction": 0}
        }

    def parse_text(self, text: str):
        text = text.lower()
        for key, val in self.keyword_map.items():
            if key in text:
                return val
        return {"volatility": 0.3, "direction": 0}