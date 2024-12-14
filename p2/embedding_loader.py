import numpy as np

class GloveLoader:
    def load(self, path: str):
        embeddings = {}
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                values = line.split()
                embeddings[values[0]] = np.asarray(values[1:], dtype='float32')
        return embeddings