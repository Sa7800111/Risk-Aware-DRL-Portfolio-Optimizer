import multiprocessing

class MarsWorkQueue:
    def __init__(self):
        self.queue = multiprocessing.Queue()

    def put_task(self, task):
        self.queue.put(task)