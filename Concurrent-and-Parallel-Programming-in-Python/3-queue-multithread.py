import threading
import time
import queue

# Function to simulate tasks
def worker(q):
    while True:
        item = q.get()
        if item is None:
            break  # End the loop if None is received
        print(f"Processing item: {item}")
        time.sleep(1)  # Simulate task duration
        q.task_done()

# Create a queue instance
task_queue = queue.Queue()

# Create worker threads
num_worker_threads = 3
threads = []
for i in range(num_worker_threads):
    t = threading.Thread(target=worker, args=(task_queue,))
    t.start()
    threads.append(t)

# Enqueue tasks
for item in range(10):
    task_queue.put(item)

# Block until all tasks are done
task_queue.join()

# Stop workers
for i in range(num_worker_threads):
    task_queue.put(None)
for t in threads:
    t.join()
