from modules.agents.environment_agent import (
    EnvironmentAgent
)

from core.world_state import (
    get_state
)

from core.focus_state import (
    get_focus
)

agent = EnvironmentAgent()

agent.observe_browser(

    website="google",

    focused_element="google_search_box"
)

print(
    get_state()
)

print(
    get_focus()
)