from sklearn.cluster import AffinityPropagation

class SectorClusterer:
    def __init__(self, matrix: np.ndarray):
        self.model = AffinityPropagation(affinity='precomputed')
        self.matrix = matrix

    def get_clusters(self):
        return self.model.fit_predict(self.matrix)