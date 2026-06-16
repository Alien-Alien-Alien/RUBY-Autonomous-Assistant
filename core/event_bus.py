import asyncio


subscribers = {}

event_bus_queue = asyncio.Queue()


def subscribe(event_type, handler):

    if event_type not in subscribers:

        subscribers[event_type] = []

    subscribers[event_type].append(handler)



async def emit(event_type, data=None):

    await event_bus_queue.put({

        "event_type": event_type,

        "data": data
    })

async def event_bus_worker():

    try:

        while True:

            event = await event_bus_queue.get()

            event_type = event["event_type"]

            data = event["data"]

            if event_type in subscribers:

                for handler in subscribers[event_type]:

                    try:

                        if asyncio.iscoroutinefunction(handler):

                            await handler(data)

                        else:

                            handler(data)

                    except Exception as e:

                        print(f"Event Bus Error: {e}")

            event_bus_queue.task_done()

    except asyncio.CancelledError:

        print("\nEvent bus stopped.\n")