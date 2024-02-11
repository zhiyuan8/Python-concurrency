import threading
import time
import queue


class ThreadSafeCounter:
    """Thread-safe counter using a lock."""

    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self, n):
        """Increment the counter with a lock to prevent race conditions."""
        for _ in range(n):
            with self.lock:
                self.value += 1


class QueueCounter:
    """Thread-safe counter using a queue with batch processing for efficiency."""

    def __init__(self):
        self.value = 0
        self.queue = queue.Queue()
        self.worker_thread = threading.Thread(target=self.worker)
        self.stop_request = threading.Event()

    def increment(self, n):
        """Enqueue a single batch increment request."""
        self.queue.put(n)

    def worker(self):
        """Process batch increment requests from the queue."""
        while not self.stop_request.is_set() or not self.queue.empty():
            try:
                increment = self.queue.get(timeout=0.05)
                self.value += increment
                self.queue.task_done()
            except queue.Empty:
                continue

    def start_worker(self):
        """Start the worker thread."""
        self.worker_thread.start()

    def stop_worker(self):
        """Signal the worker thread to stop and wait for it to finish."""
        self.stop_request.set()
        self.worker_thread.join()


def run_threaded_increments(counter, num_threads=4, increments_per_thread=100000):
    """Run increment function in a multi-threading context and measure execution time."""
    if isinstance(counter, QueueCounter):
        counter.start_worker()

    threads = [
        threading.Thread(target=counter.increment, args=(increments_per_thread,))
        for _ in range(num_threads)
    ]

    start_time = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    if isinstance(counter, QueueCounter):
        counter.stop_worker()

    end_time = time.time()

    print(f"Counter value: {counter.value}")
    print(f"Execution time: {end_time - start_time} seconds")


if __name__ == "__main__":
    # Lock-based counter test
    print("Running test with lock-based increment")
    counter_lock = ThreadSafeCounter()
    run_threaded_increments(counter_lock)

    # Queue-based counter test
    print("\nRunning test with queue-based increment")
    counter_queue = QueueCounter()
    run_threaded_increments(counter_queue)
