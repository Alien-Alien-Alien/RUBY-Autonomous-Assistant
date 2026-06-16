import asyncio

from core.lifecycle_manager import (

    set_plugin_state,

    show_plugin_states
)

from core.recovery_supervisor import (

    RecoverySupervisor
)

from core.bootstrap import (

    initialize_runtime,

    shutdown_runtime
)

async def simulate_failure():

    await asyncio.sleep(3)

    print(

        "\n[Simulated Failure]\n"
    )

    set_plugin_state(

        "voice_plugin",

        "failed"
    )


async def main():

    initialize_runtime()

    supervisor = RecoverySupervisor()


    monitor_task = asyncio.create_task(

        supervisor.monitor_loop()
    )


    failure_task = asyncio.create_task(

        simulate_failure()
    )


    await asyncio.sleep(15)


    supervisor.stop()

    monitor_task.cancel()
    await shutdown_runtime()


    print(

        "\nFinal States:\n"
    )

    print(

        show_plugin_states()
    )


asyncio.run(main())