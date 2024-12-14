import csv
import os

class AuditLogger:
    def __init__(self, log_dir: str):
        self.log_dir = log_dir
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        self.trade_file = open(os.path.join(log_dir, 'trades.csv'), 'a', newline='')
        self.writer = csv.DictWriter(self.trade_file, fieldnames=['tid', 'ts', 'p', 'q', 'taker', 'maker', 'side'])

    def log_trade(self, trade: dict):
        self.writer.writerow(trade)
        self.trade_file.flush()