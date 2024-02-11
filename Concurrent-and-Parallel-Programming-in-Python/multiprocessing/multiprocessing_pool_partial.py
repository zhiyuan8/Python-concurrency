from multiprocessing import Pool, cpu_count
import time
import logging
from functools import partial


def setup_logging():
    """Configure basic logging for the application."""
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )


def sleep_a_bit(sleep_time, start_msg="Starting sleep", end_msg="Ending sleep"):
    """Pauses execution for a specified number of seconds, logging before and after."""
    logging.info(f"{start_msg}, sleeping for {sleep_time}s")
    time.sleep(sleep_time)
    logging.info(end_msg)


def init_worker():
    """Initialize logging configuration for each worker in the pool."""
    setup_logging()


if __name__ == "__main__":
    setup_logging()

    # Pre-configure sleep_a_bit functions with fixed sleep times using partial
    sleep_tasks = [
        partial(
            sleep_a_bit, sleep_time=1, start_msg="Short nap", end_msg="Short nap done"
        ),
        partial(
            sleep_a_bit, sleep_time=3, start_msg="Medium nap", end_msg="Medium nap done"
        ),
        partial(
            sleep_a_bit, sleep_time=5, start_msg="Long nap", end_msg="Long nap done"
        ),
    ]

    num_cpu_cores = max(1, cpu_count() - 1)  # Reserve one CPU for the main process
    logging.info(f"Starting multiprocessing with {num_cpu_cores} cores")

    with Pool(num_cpu_cores, initializer=init_worker) as pool:
        # Execute pre-configured partial functions directly
        for task in sleep_tasks:
            pool.apply_async(
                task
            )  # Using apply_async to schedule execution of each task

        pool.close()
        pool.join()
    # Each partial function is called without arguments

    logging.info("All tasks have completed.")
