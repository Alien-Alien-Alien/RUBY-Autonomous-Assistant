import asyncio


event_queue = asyncio.PriorityQueue()

async def event_worker():

    try:

        while True:

            priority, event = await event_queue.get()
            print(f"Processing priority {priority}")

            event_type = event["type"]

            try:

                if event_type == "command":

                    command = event["command"]

                    handler = event["handler"]

                    args = event["args"]

                    handler(command, args)

                elif event_type == "fixed_command":

                    command = event["command"]

                    handler = event["handler"]

                    handler()

                else:

                    print(f"Unknown event type: {event_type}")

            except Exception as e:

                print(f"Worker Error: {e}")

            finally:

                event_queue.task_done()

    except asyncio.CancelledError:

        print("\nEvent worker stopped.\n")
