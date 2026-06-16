from modules.agents.ui_agent import (
    UIAgent
)

from modules.automation.keyboard_controller import (
    type_text
)

agent = UIAgent()

result = agent.click_label(
    "Ask"
)

print(result)

input(
    "Check if the cursor is in the ChatGPT box, then press Enter..."
)

type_text(
    "FOCUS_TEST"
)