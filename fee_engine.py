class FeeEngine:
    def __init__(self, maker_fee_bps: float = 1.0, taker_fee_bps: float = 2.0):
        self.maker_fee = maker_fee_bps / 10000.0
        self.taker_fee = taker_fee_bps / 10000.0

    def calculate_fees(self, trade: dict) -> tuple:
        val = trade['p'] * trade['q']
        m_fee = val * self.maker_fee
        t_fee = val * self.taker_fee
        return m_fee, t_fee