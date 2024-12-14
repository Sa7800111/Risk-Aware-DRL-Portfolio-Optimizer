class InteractionPredictor:
    def predict_link(self, node_emb1, node_emb2):
        return torch.sigmoid(torch.dot(node_emb1, node_emb2))