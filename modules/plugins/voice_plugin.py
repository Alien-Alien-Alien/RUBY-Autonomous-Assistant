import asyncio

from core.event_bus import subscribe

from core.router import handle_command

from modules.voice.voice_runtime import (

    real_voice_listener,
    stop_voice_listener
)

from core.intent_matcher import match_intent

from core.capability_registry import (

    register_capability
)

voice_task = None


async def on_voice_input(data):

    raw_text = data["text"]

    text = match_intent(raw_text)

    print(f"\n[Voice Heard] {raw_text}")

    print(f"[Matched Intent] {text}\n")

    await handle_command(text)



def initialize():

    global voice_task

    subscribe(

        "voice_input",

        lambda data: asyncio.create_task(

            on_voice_input(data)
        )
    )

    try:

        loop = asyncio.get_running_loop()

        voice_task = loop.create_task(

            real_voice_listener()
        )

    except RuntimeError:

        print(

            "No async runtime available."
        )

    register_capability(

        "open_app",

        "firefox"
    )

    register_capability(

        "open_website",

        "github"
    )

    register_capability(

        "google_search"
    )
    register_capability(
        "terminal",
        "pwd"
    )

    register_capability(
        "terminal",
        "ls"
    )

    register_capability(
        "terminal",
        "whoami"
    )
    register_capability(
        "file",
        "list"
    )

    register_capability(
        "file",
        "create_folder"
    )

    register_capability(
        "file",
        "delete_folder"
    )
    register_capability(
        "python",
        "run"
    )
    register_capability(
        "file",
        "read"
    )

    register_capability(
        "file",
        "write"
    )
    register_capability(
        "project",
        "analyze"
    )
    print("Voice plugin initialized.")



async def shutdown():

    global voice_task

    stop_voice_listener()

    if voice_task:

        try:

            await voice_task

        except asyncio.CancelledError:

            pass

    print("Voice plugin stopped.")