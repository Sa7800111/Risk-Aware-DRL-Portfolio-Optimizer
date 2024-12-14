import numpy as np

class MarketTokenizer:
    def __init__(self, price_res: float = 0.01, vol_bins: int = 128):
        self.price_res = price_res
        self.vol_bins = vol_bins

    def encode_order(self, order, mid_price: float):
        p_delta = int((order.price - mid_price) / self.price_res)
        v_token = int(np.clip(np.log1p(order.qty) * 10, 0, self.vol_bins - 1))
        type_token = 0 if order.side == Side.BUY else 1
        return [type_token, p_delta, v_token]

    def decode_tokens(self, tokens, mid_price: float):
        side = Side.BUY if tokens[0] == 0 else Side.SELL
        price = mid_price + (tokens[1] * self.price_res)
        qty = int(np.exp(tokens[2] / 10.0) - 1)
        return side, price, qty