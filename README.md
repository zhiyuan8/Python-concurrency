# Python Concurrency
Notes:
- [Notion Study notes](https://www.notion.so/Python-Java-Concurrency-b883552932a44086bbe859f88851ed28?pvs=4)
- [Udemy course](https://www.udemy.com/course/concurrent-and-parallel-programming-in-python/learn/lecture/28328244#overview)
- [Udemy course code](https://github.com/PacktPublishing/Concurrent-and-Parallel-Programming-in-Python/tree/main)

- **Multiprocessing:** Utilizes multiple processes to execute tasks in parallel.
- **Multithreading:** Employs multiple threads within the same process, sharing memory space. The Python Global Interpreter Lock (GIL) limits the effectiveness of multithreading with regards to multi-core CPU utilization.
- **Multiprocessing vs Multithreading:**
  - **Memory Space:** Multiprocessing uses separate memory for each process, whereas multithreading shares memory within the process.
  - **Overhead:** Process creation and context switching have a higher overhead in multiprocessing.
  - **Use Case:** Multiprocessing is preferred for CPU-bound tasks, and multithreading is suited for I/O-bound tasks.

# Python multi-threading
- threading.active_count() returns the number of active threads in the current process.
- threading.acquire() and threading.release() can be used to acquire and release locks.
- with statement can be used to acquire and release locks in a more concise manner. use this more often than acquire and release.

<details>
<summary>Basic threading example</summary>

```python
import threading
import time

def thread_function(name):
    print(f"Thread {name}: starting")
    time.sleep(2)
    print(f"Thread {name}: finishing")

threads = []

for i in range(5):
    x = threading.Thread(target=thread_function, args=(i,))
    threads.append(x)
    x.start()

for thread in threads:
    thread.join()
```

</details>

<details>
<summary>Custom thread class example</summary>

```python
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print(f"Thread {self.name}: starting")
        time.sleep(2)
        print(f"Thread {self.name}: finishing")

threads = []

for i in range(5):
    my_thread = MyThread(name=i)
    threads.append(my_thread)
    my_thread.start()

for thread in threads:
    thread.join()
```

</details>


<details>
<summary>Custom thread class example</summary>
  
  ```python
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

  ```
</details>

# YAML

Explore YAML, a human-friendly data serialization standard used in configurations and data processing.

- [yaml tutorial with Python](https://python.land/data-processing/python-yaml)

YAML enables storing multiple documents within a single file using the `---` separator, commonly used in Kubernetes definitions. YAML is widely used for configuration files and data serialization. It's easy to read and write, making it ideal for both developers and machines.

An example config.yaml:
```
rest:
  url: "https://example.org/primenumbers/v1"
  port: 8443

prime_numbers: [2, 3, 5, 7, 11, 13, 17, 19]
```

```
{'rest': 
  { 'url': 'https://example.org/primenumbers/v1',
    'port': 8443
  },
  'prime_numbers': [2, 3, 5, 7, 11, 13, 17, 19]
}
```

YAML is also crucial in orchestration, aiding in the management and coordination of complex systems and workflows.


# Multiprocessing
- Python `multiprocessing` module
    - `Pool`
    - `cpu_count`
- Python `functiontools` module
    - `partial`

# AsyncIO & Async/Await, Coroutines and Tasks


### Python `aiohttp` module

`aiohttp` is an asynchronous HTTP Client/Server framework that supports async/await syntax.

### Python Webscraper

Leverage Python for web scraping, utilizing tools and APIs to extract data efficiently.

- [Google Map API](https://developers.google.com/maps/documentation)
- [Google Map scraping omakarcloud](https://github.com/omkarcloud/google-maps-scraper)
- [Google Map scraping botsol](https://www.botsol.com/bots/google-maps-crawler)
- [Google Map scraping Octoparse](https://www.octoparse.com/blog/google-maps-crawlers)