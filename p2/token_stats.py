from collections import Counter

class TokenStatistics:
    def __init__(self):
        self.global_counts = Counter()

    def update(self, tokens: List[str]):
        self.global_counts.update(tokens)

    def get_top_n(self, n: int):
        return self.global_counts.most_common(n)