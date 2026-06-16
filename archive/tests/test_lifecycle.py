from core.bootstrap import (

    initialize_runtime,

    shutdown_runtime
)

from core.lifecycle_manager import (

    show_plugin_states
)

import asyncio


async def main():

    initialize_runtime()

    print(

        "\nPlugin States:\n"
    )

    print(

        show_plugin_states()
    )


    await shutdown_runtime()

    print(

        "\nAfter Shutdown:\n"
    )

    print(

        show_plugin_states()
    )


asyncio.run(main())