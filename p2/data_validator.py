class NewsValidator:
    def check_fields(self, item: dict):
        required = ['Date', 'Headline', 'Ticker']
        return all(k in item for k in required)