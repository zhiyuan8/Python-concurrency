# Python Concurrency
- [Notion Study notes](https://www.notion.so/Python-Java-Concurrency-b883552932a44086bbe859f88851ed28?pvs=4)
- [Udemy course](https://www.udemy.com/course/concurrent-and-parallel-programming-in-python/learn/lecture/28328244#overview)
- [Udemy course code](https://github.com/PacktPublishing/Concurrent-and-Parallel-Programming-in-Python/tree/main)

1. Python concurrency
- Multiprocessing : Multiprocessing involves using multiple processes to execute tasks in parallel.
- Multithreading :  Multithreading involves multiple threads within the same process sharing the same memory space. Python GIL (Global Interpreter Lock) makes it difficult to take advantage of multiple cores with multithreading.
- Nultiprocessing vs multithreading:
    - Memory Space: Multiprocessing uses separate memory spaces for each process, while multithreading shares memory space among threads within the same process.
    - Overhead: Process creation and context switching are more expensive for multiprocessing compared to multithreading.
    - Use Case: Choose multiprocessing for CPU-bound tasks and multithreading for I/O-bound tasks in Python.

## Python `threading` module
Create a `Threading.Thread` object and call the `start` method to start the thread. The `run` method is called when the `start` method is called. The `join` method is used to wait for the thread to finish.

```python

```

Below is an example to create customized thread class and use it to create threads.
```python

```

## YAML
- [yaml tutorial with Python](https://python.land/data-processing/python-yaml)  

### Basics
YAML is a human-friendly data serialization language for all programming languages. YAML is perfect for configuration files. Use `pyyaml` package to work with YAML files in Python. Use `safe_load` method to load a YAML file and `safe_dump` method to write a YAML file.

```python
import yaml

```
### YAML for Orchestration
Orchestration is the coordination and management of multiple computer systems, applications and/or services, stringing together multiple tasks in order to execute a larger workflow or process.
```
```

## Python webscrawler
- [Google Map API](https://developers.google.com/maps/documentation)
- [Google Map scraping omakarcloud](https://github.com/omkarcloud/google-maps-scraper)
- [Google Map scraping botsol](https://www.botsol.com/bots/google-maps-crawler)
- [Google Map scraping Octoparse](https://www.octoparse.com/blog/google-maps-crawlers)