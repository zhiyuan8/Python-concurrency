from multiprocessing import Process
import time
import os

def sleep():
    # Retrieve the current process name using os.getpid() for a unique identifier
    process_name = f'Process with PID: {os.getpid()}'
    print(f"{process_name} started")
    time.sleep(3)
    print(f"{process_name} finished")

num_processes = 3
processes = [Process(target=sleep) for _ in range(num_processes)]
for p in processes:
    p.start()
for p in processes:
    p.join()
