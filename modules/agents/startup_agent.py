from modules.automation.apps import (
    open_firefox
)

from core.world_state import (
    update_state
)


class StartupAgent:


    def prepare_browser(self):

        open_firefox()

        update_state(
            "active_app",
            "firefox"
        )

        return {

            "success": True
        }