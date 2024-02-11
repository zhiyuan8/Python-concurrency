import threading
import time


class SleepyWorker(threading.Thread):
    def __init__(self, n):
        self.n = n
        super().__init__()
        self.start()

    def sleep_a_bit(self, i):
        print(f"Starting {threading.current_thread().name}")
        time.sleep(i)
        print(f"{threading.current_thread().name} finished: Slept for {i} seconds")

    def run(self):
        self.sleep_a_bit(self.n)
