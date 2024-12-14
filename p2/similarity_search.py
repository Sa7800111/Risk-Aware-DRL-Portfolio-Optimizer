from scipy.spatial.distance import cosine

class AssetSimilarity:
    @staticmethod
    def compute(vec1: np.ndarray, vec2: np.ndarray):
        return 1 - cosine(vec1, vec2)