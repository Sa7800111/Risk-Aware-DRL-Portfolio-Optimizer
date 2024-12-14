import pickle

class NLPCache:
    def save(self, data, path: str):
        with open(path, 'wb') as f:
            pickle.dump(data, f)