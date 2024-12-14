import pandas as pd
import numpy as np

class DiscoveryBacktester:
    def __init__(self, signal_df: pd.DataFrame, price_df: pd.DataFrame):
        self.signals = signal_df
        self.prices = price_df
        self.results = []

    def run_event_study(self, window_size: int = 5):
        for idx, row in self.signals.iterrows():
            ticker = row['ticker']
            event_date = row['date']
            if ticker in self.prices.columns:
                subset = self.prices[ticker].loc[event_date:].head(window_size)
                returns = subset.pct_change().fillna(0)
                self.results.append({
                    "signal_val": row['sentiment'],
                    "fwd_return": returns.sum(),
                    "max_drawdown": returns.min()
                })
        return pd.DataFrame(self.results)