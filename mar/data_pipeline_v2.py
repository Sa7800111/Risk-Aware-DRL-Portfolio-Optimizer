class DataIngestor:
    def stream_csv(self, path: str):
        return pd.read_csv(path, chunksize=1000)