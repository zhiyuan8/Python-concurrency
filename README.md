# Python Concurrency
Notes:
- [Notion Study notes](https://www.notion.so/Python-Java-Concurrency-b883552932a44086bbe859f88851ed28?pvs=4)
- [Udemy course](https://www.udemy.com/course/concurrent-and-parallel-programming-in-python/learn/lecture/28328244#overview)
- [Udemy course code](https://github.com/PacktPublishing/Concurrent-and-Parallel-Programming-in-Python/tree/main)

## Topics

### 1. Python concurrency
- **Multiprocessing:** Utilizes multiple processes to execute tasks in parallel.
- **Multithreading:** Employs multiple threads within the same process, sharing memory space. The Python Global Interpreter Lock (GIL) limits the effectiveness of multithreading with regards to multi-core CPU utilization.
- **Multiprocessing vs Multithreading:**
  - **Memory Space:** Multiprocessing uses separate memory for each process, whereas multithreading shares memory within the process.
  - **Overhead:** Process creation and context switching have a higher overhead in multiprocessing.
  - **Use Case:** Multiprocessing is preferred for CPU-bound tasks, and multithreading is suited for I/O-bound tasks.

### YAML

Explore YAML, a human-friendly data serialization standard used in configurations and data processing.

- [yaml tutorial with Python](https://python.land/data-processing/python-yaml)

YAML enables storing multiple documents within a single file using the `---` separator, commonly used in Kubernetes definitions.

### Python `threading` module

The `threading` module in Python allows for the creation and management of threads for concurrent execution.

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

### Python `aiohttp` module

`aiohttp` is an asynchronous HTTP Client/Server framework that supports async/await syntax.

### YAML Basics and Orchestration

YAML is widely used for configuration files and data serialization. It's easy to read and write, making it ideal for both developers and machines.

<details>
<summary>Basic YAML handling with `pyyaml`</summary>

```python
import yaml

# Example code for YAML processing
```

</details>

YAML is also crucial in orchestration, aiding in the management and coordination of complex systems and workflows.

### Python Webscraper

Leverage Python for web scraping, utilizing tools and APIs to extract data efficiently.

- [Google Map API](https://developers.google.com/maps/documentation)
- [Google Map scraping omakarcloud](https://github.com/omkarcloud/google-maps-scraper)
- [Google Map scraping botsol](https://www.botsol.com/bots/google-maps-crawler)
- [Google Map scraping Octoparse](https://www.octoparse.com/blog/google-maps-crawlers)