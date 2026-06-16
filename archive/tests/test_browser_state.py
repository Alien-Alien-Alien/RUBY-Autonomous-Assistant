
from core.world_state import (
    update_state
)

from modules.agents.browser_state_agent import (
    BrowserStateAgent
)

update_state(
    "active_app",
    "firefox"
)

update_state(
    "current_website",
    "google"
)

agent = BrowserStateAgent()

print(
    agent.is_browser_active()
)

print(
    agent.get_browser_state()
)