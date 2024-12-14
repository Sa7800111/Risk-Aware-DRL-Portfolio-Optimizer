import pandas as pd
import os

class NewsLoader:
    def __init__(self, data_path: str):
        self.data_path = data_path

    def load_csv_batch(self, filename: str, chunk_size: int = 5000):
        full_path = os.path.join(self.data_path, filename)
        return pd.read_csv(full_path, chunksize=chunk_size, parse_dates=['Date'])

    def filter_by_ticker(self, df: pd.DataFrame, ticker: str):
        return df[df['Ticker'] == ticker]