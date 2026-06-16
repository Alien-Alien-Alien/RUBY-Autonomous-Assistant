import time
import threading

from modules.agents.adaptive_planner import (
    AdaptivePlanner
)

from modules.agents.chat_agent import (
    ChatAgent
)

from modules.agents.response_agent import (
    ResponseAgent
)

from core.intent_executor import (
    execute_intent
)

from modules.voice.tts import (
    speak
)


class AgentController:
    
    def __init__(self):

        self.chat = ChatAgent()

        self.planner = AdaptivePlanner()

        self.response_agent = (
            ResponseAgent()
        )

    async def process(

        self,

        command
    ):
        chat_starters = [

            "hello",
            "hi",
            "hey",
            "how are you",
            "what is",
            "who is",
            "why",
            "how",
            "tell me"
        ]

        if any(
            command.lower().startswith(x)
            for x in chat_starters
        ):

            reply = self.chat.reply(
                command
            )

            print(
                "\nAssistant:\n"
            )

            print(reply)

            return

        plan = self.planner.recover(
            command
        )
        supported_intents = [

            "open_app",

            "open_website",

            "python",

            "terminal",

            "file",

            "project",

            "google_search"
        ]

        plan.tasks = [

            task

            for task in plan.tasks

            if task.intent in supported_intents
        ]

        if not plan.tasks:

            start = time.time()

            chat = ChatAgent()

            reply = chat.reply(
                command
            )

            print(
                "\nAssistant:\n"
            )

            print(
                reply
            )

            threading.Thread(
                target=speak,
                args=(reply,),
                daemon=True
            ).start()

            print(
                f"\nTIME: {time.time() - start:.2f}s"
            )

            return

        response = (
            self.response_agent
            .respond(result)
        )

        for task in plan.tasks:

            result = execute_intent(
                task.__dict__
            )

            response = (
                response_agent
                .respond(result)
            )

            print(
                "\nAssistant:\n"
            )

            print(
                response
            )

            threading.Thread(
                target=speak,
                args=(response,),
                daemon=True
            ).start()