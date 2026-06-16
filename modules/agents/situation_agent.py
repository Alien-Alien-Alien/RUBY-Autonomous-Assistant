from core.world_state import (
    get_state
)

from core.focus_state import (
    get_focus
)


class SituationAgent:


    def analyze(self):

        state = get_state()

        focus = get_focus()

        active_app = state.get(
            "active_app"
        )

        website = state.get(
            "current_website"
        )

        last_search = state.get(
            "last_search"
        )

        situation = []

        if active_app:

            situation.append(
                f"Active app: {active_app}"
            )

        if website:

            situation.append(
                f"Website: {website}"
            )

        if last_search:

            situation.append(
                f"Last search: {last_search}"
            )

        if focus:

            situation.append(
                f"Focused element: {focus}"
            )

        if not situation:

            situation.append(
                "No environment information available"
            )

        return {

            "success": True,

            "summary":
            " | ".join(
                situation
            ),

            "state": state
        }