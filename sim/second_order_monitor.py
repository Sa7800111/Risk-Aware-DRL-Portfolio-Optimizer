class SecondOrderMonitor:
    def __init__(self):
        self.cascades = []

    def detect_cascade(self, trades: list):
        if len(trades) > 50 and all(t['side'] == trades[0]['side'] for t in trades):
            self.cascades.append(time.time_ns())
            return True
        return False