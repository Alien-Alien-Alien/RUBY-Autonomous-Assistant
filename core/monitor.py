import asyncio


async def system_monitor():

    try:

        while True:

            print("\n[Monitor] Assistant Running...\n")

            await asyncio.sleep(5)

    except asyncio.CancelledError:

        print("\nMonitor stopped.\n")