class NewsPipeline:
    def __init__(self, loader: NewsLoader, processor: NewsBatchProcessor):
        self.loader = loader
        self.processor = processor

    def run(self, filename: str):
        for batch in self.loader.load_csv_batch(filename):
            self.processor.process_batch(batch.to_dict('records'))