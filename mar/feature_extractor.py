class ApplicationFeatures:
    def extract_order_imbalance(self, lob: dict):
        return (lob['bid_vol'] - lob['ask_vol']) / (lob['bid_vol'] + lob['ask_vol'])