import asyncio

from modules.memory.long_term_memory import load_memory

from modules.agents.planner_agent import PlannerAgent

from modules.agents.execution_agent import ExecutionAgent

from modules.agents.monitor_agent import MonitorAgent

from core.event_bus import (

    subscribe,

    event_bus_worker
)


async def main():

    load_memory()


    planner = PlannerAgent()

    executor = ExecutionAgent()

    monitor = MonitorAgent()


    subscribe(

        "planning",

        monitor.handle_event
    )

    subscribe(

        "execution",

        monitor.handle_event
    )

    subscribe(

        "recovery",

        monitor.handle_event
    )


    bus_task = asyncio.create_task(

        event_bus_worker()
    )


    plan = planner.plan(

        "search robotics papers"
    )


    print("\nGenerated Plan:\n")

    print(plan)


    tasks = plan["tasks"]


    for task in tasks:

        executor.execute(task)


    await asyncio.sleep(2)

    bus_task.cancel()


asyncio.run(main())