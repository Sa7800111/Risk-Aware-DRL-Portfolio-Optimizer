class UserOrderInjector:
    def __init__(self, gateway: MarsGateway):
        self.gateway = gateway

    def manual_inject(self, ticker: str, side: int, price: float, qty: int):
        order_data = {
            "side": side,
            "price": price,
            "qty": qty,
            "type": 1,
            "cid": "USER_INTERACTION"
        }
        return self.gateway.handle_request(ticker, order_data)