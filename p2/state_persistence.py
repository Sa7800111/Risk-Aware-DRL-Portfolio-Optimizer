import json

class GraphSerializer:
    def save_graph(self, nodes: dict, path: str):
        data = {k: v.adjacency_list for k, v in nodes.items()}
        with open(path, 'w') as f: json.dump(data, f)