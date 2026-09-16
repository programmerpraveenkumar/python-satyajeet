import time

import asyncio
async def task1():
    print("task1 start")
    await asyncio.sleep(10)
    print("task1 end")

async def task2():
    print("task2 start")
    await asyncio.sleep(2)
    print("task2 end")

async def main():
    await asyncio.gather(task1(), task2())


asyncio.run(main())

"""

unit testing
deplpyment
sockets
streamingresponse
async/await

Recat
"""
