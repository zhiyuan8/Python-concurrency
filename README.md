# Python concurrency
Concurrency in Python is achieved through **Multiprocessing**, **Multithreading**, and **Asynchronous Programming**, each suited to different scenarios based on the nature of tasks and the desired efficiency.

Referenes:
- [Zack's Notion Study notes](https://www.notion.so/Python-Java-Concurrency-b883552932a44086bbe859f88851ed28?pvs=4)
- [Udemy course](https://www.udemy.com/course/concurrent-and-parallel-programming-in-python/learn/lecture/28328244#overview)
- [Udemy course github code](https://github.com/PacktPublishing/Concurrent-and-Parallel-Programming-in-Python/tree/main)
- [Python Asyncio: The Complete Guide](https://superfastpython.com/python-asyncio/)  
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [Python multiprocessing official doc](https://docs.python.org/3/library/multiprocessing.html)
- [Python threading official doc](https://docs.python.org/3/library/threading.html)
- [Python asyncio official doc](https://docs.python.org/3/library/asyncio.html)
- [Python Coroutines and Tasks](https://docs.python.org/3/library/asyncio-task.html)
- [Python aiohttp](https://docs.aiohttp.org/en/stable/)


### Multiprocessing

Multiprocessing allows for parallel execution of tasks across multiple CPU cores, each process having its own memory space.

- **Key Components:**
  - **Pool**: Simplifies the process of spawning multiple tasks across processes. It provides a means to parallelize the execution of a function across multiple input values, distributing the input data across processes (data parallelism).
    - **Usage**: `Pool` can be used to manage a pool of worker processes for tasks that are CPU-bound and require parallel execution to speed up the processing.
  - **Process**: Represents an activity that is run in a separate process.
  - **Pipe** and **Queue**: Mechanisms for inter-process communication (IPC). A `Pipe` is used for bi-directional communication between two processes. A `Queue` is used for multiple producers and consumers.

```python
from multiprocessing import Pool
from functools import partial

def square_number(n, multiplier):
    return n * n * multiplier

if __name__ == "__main__":
    multiplier = 2
    partial_square_number = partial(square_number, multiplier=multiplier)
    
    with Pool(processes=4) as pool:  # Use 4 worker processes
        results = pool.map(partial_square_number, range(10))
        print(results)
```

### Multithreading

Multithreading involves running multiple threads (lighter weight than processes) within the same process, sharing memory space.

- **Key Component:**
  - **threading**: Python module that provides a way of using threads to achieve concurrency. Threads share the same memory space and are lighter weight than processes.
- **Synchronization Primitives:**
  - **Lock** and **Semaphore**: Essential for preventing race conditions and ensuring thread safety by controlling access to shared resources.

### Multiprocessing vs Multithreading

- **Memory Space**: Separate for multiprocessing, shared for multithreading.
- **Overhead**: Generally higher for multiprocessing due to the cost of starting and managing new processes.
- **Use Case**: Multiprocessing is preferred for CPU-bound tasks, while multithreading is better suited for I/O-bound tasks.

### Asynchronous Programming

- **asyncio**: A library to write concurrent code using the async/await syntax.
- **Key Concepts:**
  - **async/await**: Enables asynchronous programming, allowing the program to run other tasks while waiting for an operation to complete.
  - **Event Loop**: Orchestrates the execution of various tasks and handles all the I/O operations asynchronously.
  - **Coroutines and Tasks**: The building blocks for asynchronous programming in Python.
    - **Example Coroutine**:
      ```python
      async def fetch_data():
          await asyncio.sleep(1)
          return {'data': 'sample'}
      ```

### asyncio I/O and aiohttp

- **asyncio I/O**: Facilitates non-blocking I/O operations, significantly improving the efficiency of I/O-bound tasks.
- **aiohttp Usage**: For asynchronous HTTP requests. It supports both client and server-side operations.
  - **Example aiohttp Client Usage**:
    ```python
    async def fetch_page(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()
    ```

This improved markdown format not only enhances readability but also provides clear, actionable information on the key components and use cases of Python's concurrency models, including practical examples of using `Pool` for multiprocessing, making HTTP requests with `aiohttp`, and writing coroutines.
To enhance the quality of your markdown and add more detailed explanations for the concepts, I've reformatted and expanded on your notes. Here's an improved version that should make the information clearer and more comprehensive:

---

# Python Concurrency Implementations

## Multiprocessing
Explore the `multiprocessing` module in Python, which allows for the execution of multiple processes simultaneously, leveraging multiple CPU cores.

- **Python `multiprocessing` module**:
  - **`Pool`**: A convenient way to parallelize executing a function across multiple input values, distributing the input data across processes (data parallelism).
  - **`cpu_count`**: Returns the number of CPU cores available on your system. This can be helpful to decide the number of processes to run in parallel.
  - **`await`**: Not applicable here as `await` is used with asyncio for asynchronous programming. Multiprocessing deals with concurrent execution in separate processes.

- **Python `functools` module**:
  - **`partial`**: Used to create a partial function by fixing some portion of a function's arguments, which can be particularly useful in multiprocessing when you want to pass additional fixed arguments to the function being executed by the pool.

## Python Multi-threading
Multi-threading in Python allows multiple threads to run concurrently in a single process, sharing the same space.

- **Key Functions**:
  - `threading.active_count()`: Returns the number of Thread objects currently alive.
  - The combination of `threading.Lock().acquire()` and `threading.Lock().release()` manages locks explicitly. However, using the `with` statement for lock management is more concise and less error-prone, as it ensures that the lock is released automatically.

### Basic Threading Example
<details>
<summary>Click to expand</summary>

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

### Custom Thread Class Example
<details>
<summary>Click to expand</summary>

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

### Threading with Lock Management
<details>
<summary>Click to expand</summary>

```python
import threading
import time

class ThreadSafeCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self, n):
        for _ in range(n):
            with self.lock:
                self.value += 1

def run_threaded_increments(counter, increments):
    threads = [threading.Thread(target=counter.increment, args=(increments,)) for _ in range(4)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    counter = ThreadSafeCounter()
    run_threaded_increments(counter, 100000)
    print(f"Counter value: {counter.value}")
```
</details>

## YAML
YAML, a human-friendly data serialization standard, is widely used in configurations and data processing, supporting multiple documents within a single file with the `---` separator.

<details>
<summary>Click to expand</summary>

```yaml
rest:
  url: "https://example.org/primenumbers/v1"
  port: 8443

prime_numbers: [2, 3, 5, 7, 11, 13, 17, 19]
```
</details>

## AsyncIO & Multi-threading
AsyncIO provides a framework for writing single-threaded concurrent code using coroutines, event loops, and I/O completion callbacks. Multi-threading runs multiple threads in a single process.

### Python `aiohttp` module
`aiohttp` is an asynchronous HTTP Client/Server framework that supports the async/await syntax, ideal for non-blocking HTTP requests.

### Coroutine
In Python, a coroutine is a special function that can be paused and resumed, allowing other code to run during the pauses. This can be useful for tasks that spend a lot of time waiting for something (like user input, file I/O, network responses, etc.), as it allows other tasks to make progress during the waiting periods.

Coroutines in Python are defined using the async def syntax:
```
async def my_coroutine():
    ...
```
Within a coroutine, the await keyword can be used to pause execution until some other function (often another coroutine) is complete:
```
async def my_coroutine():
    await some_other_function()
```
When some_other_function() is called with the await keyword, my_coroutine() is paused. When some_other_function() is done, my_coroutine() is resumed where it left off.  



# Python Web Scraper
Leveraging Python for web scraping involves using libraries and APIs to extract data efficiently from web pages.