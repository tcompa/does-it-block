import asyncio
import time
from does_it_block import does_it_block


async def sleep_three_sync():
    print("sleep_three_sync - START")
    time.sleep(3)
    print("sleep_three_sync - END")


async def sleep_three_async():
    print("sleep_three_async - START")
    await asyncio.sleep(3)
    print("sleep_three_async - END")


if __name__ == "__main__":
    asyncio.run(does_it_block(sleep_three_sync))
    asyncio.run(does_it_block(sleep_three_async))