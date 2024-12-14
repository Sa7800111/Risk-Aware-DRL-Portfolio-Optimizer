import spacy

class EntityExtractor:
    def __init__(self, model: str = "en_core_web_sm"):
        self.nlp = spacy.load(model)

    def extract_tickers(self, text: str) -> List[str]:
        doc = self.nlp(text)
        entities = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
        return list(set(entities))