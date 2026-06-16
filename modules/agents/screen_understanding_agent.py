from modules.agents.chat_agent import ChatAgent

from modules.memory.screen_context_memory import (
    ScreenContextMemory
)


class ScreenUnderstandingAgent:

    def __init__(self):

        self.chat = ChatAgent()

        self.memory = (
            ScreenContextMemory()
        )

    def understand(self, screen_text):

        prompt = f"""
You are a desktop state analyzer.

Only use information explicitly present in the screen text.

Do NOT guess.
Do NOT speculate.
Do NOT infer crimes, intentions, emotions, or hidden activities.

SCREEN:

{screen_text}

Return:

Current activity:
Open tools:
Visible files/projects:

If information is missing say:
Unknown
"""

        response = self.chat.reply(
            prompt
        )

        self.memory.add(
            response
        )

        return response

    def get_recent_context(self):

        return (
            self.memory.get_activity_chain()
        )