from multiprocessing import Pool, cpu_count
import time
import os
import logging
from functools import partial
from random import randint

def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def sleep_a_bit(*args):
    for n in args:
        time.sleep(n)

def process_task(process_id, sleep_times):
    total_sleep_time = sum(sleep_times)
    start_message = f"Task {process_id} started, sleeping for {total_sleep_time}s"
    sleep_a_bit(*sleep_times)
    finished_message = f"Task {process_id} finished"
    return [start_message, finished_message]

def process_task_wrapper(args):
    return process_task(*args)

if __name__ == "__main__":
    setup_logging()
    num_cpu_cores = max(1, cpu_count() - 1)
    logging.info(f"Number of CPUs being used: {num_cpu_cores}")

    num_tasks = 3
    tasks_with_sleep_times = [(i, [randint(1, 5) for _ in range(randint(1, 3))]) for i in range(num_tasks)]

    # If there were common setup parameters for process_task, you'd use partial here, like:
    # task_func = partial(process_task_wrapper, common_param=common_value)
    # But since there's not in this case, we directly use process_task_wrapper

    with Pool(num_cpu_cores) as pool:
        results = pool.map(process_task_wrapper, tasks_with_sleep_times)

    for result in results:
        for message in result:
            logging.info(message)

    logging.info("All tasks have completed.")
