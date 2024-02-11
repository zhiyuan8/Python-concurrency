import asyncio
import time
import os
import threading  # Import the threading module to access thread-related utilities

async def async_sleep(n):
    pid = os.getpid()  # Get the current process ID
    thread_id = threading.get_native_id()  # Get the current thread ID
    print(f"PID: {pid}, Thread ID: {thread_id} - Start sleeping for {n} seconds")
    await asyncio.sleep(3)
    print(f"PID: {pid}, Thread ID: {thread_id} - Finished sleeping")

async def return_hello():
    pid = os.getpid()  # Get the current process ID
    thread_id = threading.get_native_id()  # Get the current thread ID
    print(f"PID: {pid}, Thread ID: {thread_id} - return_hello() is called")
    return "Hello"

async def main():
    start_time = time.time()
    try:
        await asyncio.gather(
            asyncio.wait_for(async_sleep(1), timeout=1), # if the timeout is reached, a TimeoutError is raised
            asyncio.wait_for(async_sleep(3), timeout=1),
            asyncio.wait_for(async_sleep(5), timeout=1),
            return_hello())
    except asyncio.TimeoutError:
        print("TimeoutError occurred")
    # Print the PID and Thread ID for the main function
    print(f"Main function PID: {os.getpid()}, Thread ID: {threading.get_native_id()}")

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print(f"Program completed in {time.time() - start_time} seconds with PID: {os.getpid()}, Thread ID: {threading.get_native_id()}")
