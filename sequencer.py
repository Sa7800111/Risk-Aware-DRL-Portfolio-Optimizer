import queue
import threading

class TransactionSequencer:
    def __init__(self):
        self.inbox = queue.PriorityQueue()
        self.running = False
        self._lock = threading.Lock()

    def push(self, priority: int, payload: dict):
        with self._lock:
            self.inbox.put((priority, time.time_ns(), payload))

    def poll(self):
        try:
            return self.inbox.get(block=False)
        except queue.Empty:
            return None