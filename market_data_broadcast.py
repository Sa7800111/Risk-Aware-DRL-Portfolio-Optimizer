import json
import zmq

class MarketDataPublisher:
    def __init__(self, port: int = 5556):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind(f"tcp://*:{port}")

    def publish_update(self, ticker: str, depth: dict):
        payload = {"ticker": ticker, "data": depth, "ts": time.time_ns()}
        self.socket.send_string(f"LOB_UPDATE {json.dumps(payload)}")

    def publish_trade(self, ticker: str, trade: dict):
        payload = {"ticker": ticker, "trade": trade}
        self.socket.send_string(f"TRADE_UPDATE {json.dumps(payload)}")