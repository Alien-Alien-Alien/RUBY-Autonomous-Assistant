from core.world_state import (
    get_state
)


class BrowserStateAgent:


    def is_browser_active(self):

        state = get_state()

        return (

            state.get(
                "active_app"
            ) == "firefox"
        )


    def get_browser_state(self):

        state = get_state()

        return {

            "active_app":
            state.get(
                "active_app"
            ),

            "current_website":
            state.get(
                "current_website"
            ),

            "last_search":
            state.get(
                "last_search"
            )
        }