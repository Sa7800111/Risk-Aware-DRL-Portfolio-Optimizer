import re

class PatternMatcher:
    def __init__(self):
        self.price_pattern = re.compile(r'\$\d+(?:\.\d+)?')
        self.pct_pattern = re.compile(r'\d+(?:\.\d+)?%')

    def find_targets(self, text: str):
        return {
            "prices": self.price_pattern.findall(text),
            "percentages": self.pct_pattern.findall(text)
        }