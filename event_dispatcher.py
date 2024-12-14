class EventDispatcher:
    def __init__(self):
        self.subscribers = {"TRADE": [], "ORDER_REJECT": [], "BOOK_UPDATE": []}

    def subscribe(self, event_type: str, callback):
        if event_type in self.subscribers:
            self.subscribers[event_type].append(callback)

    def emit(self, event_type: str, data: dict):
        for callback in self.subscribers.get(event_type, []):
            callback(data)