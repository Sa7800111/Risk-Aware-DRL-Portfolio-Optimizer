class RelationshipMap:
    def __init__(self):
        self.mapping = {"SUPPLIER": 0.8, "COMPETITOR": -0.5, "PARTNER": 0.6}

    def get_link_strength(self, rel_type: str):
        return self.mapping.get(rel_type, 0.1)