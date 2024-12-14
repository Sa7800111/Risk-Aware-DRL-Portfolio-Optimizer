class ProtoEncoder:
    def encode_signal(self, ticker, timestamp, vector):
        # Logic for Protobuf encoding for high-speed streaming
        return f"{ticker}|{timestamp}|{vector.tolist()}"