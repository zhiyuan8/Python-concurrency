import asyncio
import time

async def async_sleep():
    print("Start sleeping for 3 seconds")
    # Using asyncio.sleep for asynchronous delay
    await asyncio.sleep(3)
    print("Finished sleeping")

# If you want to call return_hello concurrently with async_sleep and use await,
# you could make it async even if it doesn't perform any awaitable actions.
# This is just to fit the async pattern, but not necessary in this context.
async def return_hello():
    return "Hello"

async def main():
    # Schedule async_sleep() to run without waiting for it to finish
    task = asyncio.create_task(async_sleep())
    
    # Execute return_hello concurrently. Since it's now an async function, you can use await.
    result = await return_hello()
    print("result: ", result)
    
    # Now wait for the async_sleep() task to complete
    await task

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print(f"Program completed in {time.time() - start_time} seconds")
