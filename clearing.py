class ClearingHouse:
    def __init__(self):
        self.accounts = {}
        self.transaction_log = []

    def register_account(self, cid: str, initial_cash: float):
        self.accounts[cid] = {"cash": initial_cash, "positions": {}}

    def process_trade(self, trade: dict):
        t_id, m_id = trade['taker'], trade['maker']
        price, qty = trade['p'], trade['q']
        
        cost = price * qty
        self.accounts[t_id]['cash'] -= cost
        self.accounts[m_id]['cash'] += cost
        self.transaction_log.append(trade)