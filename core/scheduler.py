import asyncio
from core.event_bus import emit

async def reminder_task(message, delay):

    await asyncio.sleep(delay)

    print(f"\n[Reminder] {message}\n")

    await emit("reminder_finished", {

        "message": message
    })