from multiprocessing import Process, Queue
import time
import os
import logging
from threading import Thread

def setup_logging():
    """Configure basic logging for the application."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_task(queue, process_id):
    """
    Simulates a task performed by a process.
    
    Args:
        queue (Queue): A multiprocessing queue for inter-process communication.
        process_id (int): An identifier for the current process.
    """
    process_name = f'Process with PID: {os.getpid()}, ID: {process_id}'
    start_message = f"{process_name} started"
    queue.put(start_message)
    time.sleep(10)  # Simulate work being done
    finished_message = f"{process_name} finished"
    queue.put(finished_message)
    queue.put("SENTINEL")  # Send a sentinel value to indicate process completion

def monitor_queue(queue, num_processes):
    """
    Monitors the queue for messages and logs them as they arrive,
    and waits for a specific number of sentinel values before exiting.
    
    Args:
        queue (Queue): A multiprocessing queue to monitor.
        num_processes (int): The number of processes to wait for.
    """
    sentinel_received = 0
    while sentinel_received < num_processes:
        message = queue.get()  # This will block until an item is available
        if message == "SENTINEL":
            sentinel_received += 1
            continue
        logging.info(message)
    logging.info("Monitoring completed.")

if __name__ == "__main__":
    setup_logging()
    num_processes = 3
    q = Queue()

    processes = [Process(target=process_task, args=(q, i)) for i in range(num_processes)]

    for p in processes:
        p.start()

    # Start a separate thread to monitor queue messages in real-time
    monitor = Thread(target=monitor_queue, args=(q, num_processes))
    monitor.start()

    for p in processes:
        p.join()
    
    monitor.join()  # Ensure the monitor thread completes

    logging.info("All processes have completed.")
