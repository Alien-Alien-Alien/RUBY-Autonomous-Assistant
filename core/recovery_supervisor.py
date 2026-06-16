import asyncio

from core.lifecycle_manager import (
    get_plugin_state,
    set_plugin_state
)

from core.telemetry import (
    record_failure,
    record_recovery
)


class RecoverySupervisor:


    def __init__(self):

        self.running = True


    async def monitor_loop(self):

        while self.running:

            await asyncio.sleep(5)

            await self.check_plugins()


    async def check_plugins(self):

        plugins = [

            "voice_plugin",

            "reminder_plugin"
        ]


        for plugin in plugins:

            state = get_plugin_state(
                plugin
            )

            print(
                f"[Supervisor] "
                f"{plugin}: {state}"
            )


            if state == "failed":

                record_failure(
                    plugin
                )

                await self.recover_plugin(
                    plugin
                )


    async def recover_plugin(
        self,
        plugin_name
    ):

        print(
            f"[Supervisor] "
            f"Recovering {plugin_name}"
        )


        set_plugin_state(
            plugin_name,
            "recovering"
        )


        await asyncio.sleep(2)


        set_plugin_state(
            plugin_name,
            "active"
        )


        record_recovery(
            plugin_name
        )


        print(
            f"[Supervisor] "
            f"{plugin_name} restored."
        )


    def stop(self):

        self.running = False