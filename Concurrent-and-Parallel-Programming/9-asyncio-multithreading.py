import asyncio
import time
import os
import multiprocessing


class MultiprocessingAsync(multiprocessing.Process):
    def __init__(self, durations):
        super().__init__()
        self._durations = durations

    @staticmethod
    async def async_sleep(duration):  # Coroutine 1
        pid = os.getpid()  # Get the current process ID
        print(f"PID: {pid} - Start sleeping for {duration} seconds")
        await asyncio.sleep(duration)  # non-blocking sleep
        print(
            f"PID: {pid} - Finished sleeping"
        )  # you expect to see the same PID for all the tasks, as they are running in the same process
        return duration


    async def consecutive_sleeps(self):
        # Create tasks for each duration and await their completion
        tasks = [self.async_sleep(duration) for duration in self._durations]
        for task in asyncio.as_completed(tasks):
            result = await task
            print(f"Task sleeping for {result} seconds is complete")


    def run(self):
        # Run the async event loop for consecutive_sleeps
        asyncio.run(self.consecutive_sleeps())


if __name__ == "__main__":
    start_time = time.time()
    processes = []
    durations_list = [[1, 2], [2, 3]]  # Example durations for each process

    # Create and start a process for each set of durations
    for durations in durations_list:
        p = MultiprocessingAsync(durations)
        processes.append(p)
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()

    # Print the total execution time
    print(f"Program completed in {time.time() - start_time} seconds with PID: {os.getpid()}")
