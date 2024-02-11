import asyncio
import time
import os
import threading  # Import the threading module to access thread-related utilities

async def async_sleep(n): # Coroutine 1
    pid = os.getpid()  # Get the current process ID
    thread_id = threading.get_native_id()  # Get the current thread ID
    print(f"PID: {pid}, Thread ID: {thread_id} - Start sleeping for {n} seconds")
    await asyncio.sleep(n) # non-blocking sleep
    print(f"PID: {pid}, Thread ID: {thread_id} - Finished sleeping")
    return n

async def main(): # Coroutine 2
    # step 1
    # You create initial tasks for sleeping different durations (1 to 10 seconds) and add them to a set named pending.
    pending = set()
    for i in range(1,11):
        pending.add(asyncio.create_task(async_sleep(i)))
    
    add_task = True
    
    while len(pending) > 0:
        # it waits for at least one of the pending tasks to complete
        done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
        # As tasks complete (starting with the shortest sleep), they are moved to the done set, and their completion is announced.
        for done_task in done:
            print(f"Task {done_task.result()} is complete")
            if add_task:
                # After the first task completes, you add one additional task with a 1-second sleep. This is added only once due to the add_task flag ensuring it's a one-time operation.
                pending.add(asyncio.create_task(async_sleep(1)))
                add_task = False

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print(f"Program completed in {time.time() - start_time} seconds with PID: {os.getpid()}, Thread ID: {threading.get_native_id()}")