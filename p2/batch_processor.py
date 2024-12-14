class NewsBatchProcessor:
    def __init__(self, cleaner: TextCleaner, ner: EntityExtractor):
        self.cleaner = cleaner
        self.ner = ner

    def process_batch(self, raw_items: List[dict]):
        processed = []
        for item in raw_items:
            clean_text = self.cleaner.clean_headline(item['headline'])
            entities = self.ner.extract_tickers(item['body'])
            processed.append({**item, "clean_text": clean_text, "entities": entities})
        return processed