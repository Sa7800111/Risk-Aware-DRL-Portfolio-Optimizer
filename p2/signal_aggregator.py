class SignalAggregator:
    def aggregate_daily(self, signals: List[dict]):
        df = pd.DataFrame(signals)
        return df.groupby('Date').mean()