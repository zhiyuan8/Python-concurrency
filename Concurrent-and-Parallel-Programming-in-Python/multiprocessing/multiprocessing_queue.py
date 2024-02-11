from multiprocessing import Process, Queue
import time
import os

def sleep(q):
    # Retrieve the current process name using os.getpid() for a unique identifier
    process_name = f'Process with PID: {os.getpid()}'
    start_message = f"{process_name} started"
    q.put(start_message)  # Put the start message into the queue
    time.sleep(3)
    finished_message = f"{process_name} finished"
    q.put(finished_message)  # Put the finished message into the queue

if __name__ == "__main__":
    num_processes = 3
    q = Queue()  # Create a Queue object
    processes = [Process(target=sleep, args=(q,)) for _ in range(num_processes)]  # Pass the Queue as an argument to each process

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    # Read and print messages from the queue
    while not q.empty():
        print(q.get())
