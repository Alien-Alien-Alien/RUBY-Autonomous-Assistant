import asyncio


async def task_one():

    while True:

        print("Task One Running")

        await asyncio.sleep(2)



async def task_two():

    while True:

        print("Task Two Running")

        await asyncio.sleep(1)



async def main():

    await asyncio.gather(

        task_one(),

        task_two()
    )


asyncio.run(main())