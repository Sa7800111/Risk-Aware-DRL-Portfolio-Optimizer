class VocabularyBuilder:
    def __init__(self):
        self.vocab = {}
    def build(self, corpus: List[str]):
        unique = set(" ".join(corpus).split())
        self.vocab = {word: i for i, word in enumerate(unique)}