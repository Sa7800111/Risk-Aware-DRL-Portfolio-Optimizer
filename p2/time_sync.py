from datetime import timedelta

class MarketTimeAligner:
    def __init__(self, market_open: str = "09:30", market_close: str = "16:00"):
        self.open = market_open
        self.close = market_close

    def align_to_session(self, dt: datetime) -> datetime:
        if dt.time() < datetime.strptime(self.open, "%H:%M").time():
            return dt.replace(hour=9, minute=30, second=0)
        return dt