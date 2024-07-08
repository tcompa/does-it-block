import asyncio
import time



async def does_it_block(function):
    # First run (the target function, by itself)
    print(f"START running {function}, by itself")
    t_start = time.perf_counter()
    task = asyncio.create_task(function())
    await task
    elapsed_single = time.perf_counter() - t_start

    print(f"END running {function}, by itself")
    print(f"ELAPSED: {elapsed_single:.3f} seconds")
    print()

    async def monitor():
        interval = 0.1
        num_iterations = int(elapsed_single / interval)
        for i in range(num_iterations):
            # Uncomment to see all iterations
            # print(f"Monitor {i}/{num_iterations}")
            await asyncio.sleep(interval)

    # Second run (the target function, together with )
    print(f"START running {function}, concurrently")
    t_start = time.perf_counter()
    task1 = asyncio.create_task(function())
    task2 = asyncio.create_task(monitor())
    await task1
    await task2
    elapsed_concurrent = time.perf_counter() - t_start
    print(f"END running {function}, concurrently")
    print(f"ELAPSED: {elapsed_concurrent:.3f} seconds")
    print()

    print(f"ELAPSED (SINGLE):     {elapsed_single:.3f}")
    print(f"ELAPSED (CONCURRENT): {elapsed_concurrent:.3f}")

    if elapsed_concurrent / elapsed_single < 1.5:
        print("BEST GUESS: The function is non blocking")
    elif elapsed_concurrent / elapsed_single < 2.0:
        print("BEST GUESS: N/A")
    else:
        print("BEST GUESS: The function is blocking")

    print("*" * 80)
    print()
