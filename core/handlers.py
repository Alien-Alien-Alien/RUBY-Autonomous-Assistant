from core.logger import log_action
from modules.memory.session_memory import get_history
from modules.memory.context_manager import update_context,get_context
from core.scheduler import reminder_task
import asyncio
from core.grammar_registry import register_grammar

from modules.automation.terminal import run_terminal_command

from modules.automation.files import (
    create_folder,
    delete_folder
)

from modules.automation.browser import (
    google_search
)


def handle_create_folder(command, args):

    if len(args) < 1:

        print("Folder name missing.")

        return

    if args[0] == "called" and len(args) > 1:

        folder_name = args[1]

    else:

        folder_name = args[0]

    log_action(command)

    create_folder(folder_name)
    update_context("last_folder", folder_name)



def handle_delete_folder(command, args):

    if len(args) < 1:

        print("Folder name missing.")

        return

    folder_name = args[0]

    log_action(command)

    delete_folder(folder_name)



def handle_google_search(command, args):

    if len(args) < 1:

        print("Search query missing.")

        return

    query = " ".join(args)

    log_action(command)

    google_search(query)


def handle_terminal_command(command, args):

    if len(args) < 1:

        print("Terminal command missing.")

        return

    terminal_command = " ".join(args)

    log_action(command)

    run_terminal_command(terminal_command)

def handle_history(command, args):

    history = get_history()

    if len(history) == 0:

        print("No command history.")

        return

    for index, item in enumerate(history, start=1):

        print(f"{index}. {item}")

def handle_open_last_folder(command, args):

    folder_name = get_context("last_folder")

    if not folder_name:

        print("No folder in context.")

        return

    print(f"Last folder: {folder_name}")


def handle_reminder(command, args):

    if len(args) < 2:

        print("Usage: remind me <message> in <seconds>")

        return

    try:

        message = args[0]

        delay = int(args[1])

        asyncio.create_task(

            reminder_task(message, delay)
        )

        print(f"Reminder set for {delay} seconds.")

    except ValueError:

        print("Invalid time format.")



