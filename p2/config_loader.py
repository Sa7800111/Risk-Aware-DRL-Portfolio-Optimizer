import yaml

class NLPConfig:
    def __init__(self, path: str):
        with open(path) as f:
            self.settings = yaml.safe_load(f)