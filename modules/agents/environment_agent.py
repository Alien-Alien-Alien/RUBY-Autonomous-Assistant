from core.world_state import (
    update_state
)

from core.focus_state import (
    set_focus
)


class EnvironmentAgent:


    def observe_browser(

        self,

        website=None,

        focused_element=None
    ):

        if website:

            update_state(
                "current_website",
                website
            )

        if focused_element:

            set_focus(
                focused_element
            )

        return {

            "success": True
        }