import threading
import time
import queue

def worker(q):
    while True:
        item = q.get()
        if item is None:
            q.task_done()
            break
        print(f"Processing item: {item}")
        time.sleep(1)  # Simulate task duration
        q.task_done()

def main():
    task_queue = queue.Queue()
    num_worker_threads = 3

    # Create and start worker threads
    threads = []
    for _ in range(num_worker_threads):
        t = threading.Thread(target=worker, args=(task_queue,))
        t.start()
        threads.append(t)

    # Enqueue tasks
    for item in range(10):
        task_queue.put(item)

    # Block until all tasks are done
    task_queue.join()

    # Stop workers by sending a stop signal
    for _ in range(num_worker_threads):
        task_queue.put(None)

    # Wait for all threads to complete
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
