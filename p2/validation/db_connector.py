import sqlite3

class SignalDB:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS signals (ticker TEXT, date TEXT, val REAL)")