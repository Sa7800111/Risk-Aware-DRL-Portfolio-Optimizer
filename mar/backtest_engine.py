class MarsBacktester:
    def __init__(self, history_data: str):
        self.data = pd.read_csv(history_data)

    def run_strategy(self, strategy_func: callable):
        pnl = 0.0
        for i, row in self.data.iterrows():
            signal = strategy_func(row)
            pnl += self.execute_on_mars(signal)
        return pnl