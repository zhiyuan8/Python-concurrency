import threading
import time

class ThreadSafeCounter:
    """Thread-safe counter implementation."""
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment_with_lock(self, n):
        """Increment the counter with a lock to prevent race conditions."""
        for _ in range(n):
            with self.lock:
                self.value += 1

    def increment_no_lock(self, n):
        """Increment the counter without a lock, leading to potential race conditions."""
        for _ in range(n):
            self.value += 1

    def increment_with_lock_v2(self, n):
        """Increment the counter with explicit lock acquisition and release.
        acquire and lock can be very time consuming, so it is better to use with statement to avoid forgetting to release the lock."""
        for _ in range(n):
            self.lock.acquire()
            try:
                self.value += 1
            finally:
                self.lock.release()

def run_threaded_increments(func, counter):
    """Run the specified increment function in a multithreading context."""
    threads = []
    for _ in range(4):  # Create 4 threads
        thread = threading.Thread(target=func, args=(counter, 100000))
        threads.append(thread)

    start_time = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()

    print(f"Counter value: {counter.value}")
    print(f"Execution time for {func.__name__}: {end_time - start_time} seconds")

if __name__ == "__main__":
    # Run tests with different increment strategies
    for increment_method in [ThreadSafeCounter.increment_no_lock, ThreadSafeCounter.increment_with_lock, ThreadSafeCounter.increment_with_lock_v2]:
        counter = ThreadSafeCounter()  # Create a new counter for each test
        print(f"Running test with {increment_method.__name__}")
        run_threaded_increments(increment_method, counter)
