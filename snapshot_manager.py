import pickle

class SnapshotManager:
    def __init__(self, state, interval_sec: int = 60):
        self.state = state
        self.interval = interval_sec

    def take_snapshot(self, filename: str):
        data = {ticker: book.get_depth(20) for ticker, book in self.state.books.items()}
        with open(filename, 'wb') as f:
            pickle.dump(data, f)