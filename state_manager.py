import h5py
import numpy as np

class ExchangeState:
    def __init__(self, tickers: List[str]):
        self.books = {t: LimitOrderBook(t) for t in tickers}
        self.engines = {t: MatchingEngine(self.books[t]) for t in tickers}
        self.validators = {t: MarketValidator(0.01, 1) for t in tickers}

    def submit(self, ticker: str, order):
        if ticker not in self.engines:
            return False
        if self.validators[ticker].validate_order(order):
            self.engines[ticker].process_order(order)
            return True
        return False

    def save_checkpoint(self, path: str):
        with h5py.File(path, 'w') as f:
            for t, book in self.books.items():
                g = f.create_group(t)
                g.create_dataset('depth', data=np.array(list(book.get_depth().items())))