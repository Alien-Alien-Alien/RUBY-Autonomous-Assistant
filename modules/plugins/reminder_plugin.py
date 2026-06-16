from core.grammar_registry import register_grammar

from core.handlers import handle_reminder

from core.event_bus import subscribe

def register():

    register_grammar({

        "name": "reminder",

        "pattern": r"remind me to (.+) in (\d+)",

        "handler": handle_reminder
    })

def initialize():
    subscribe(

        "reminder_finished",

        on_reminder_finished
    )

    print("Reminder plugin initialized.")



def shutdown():

    print("Reminder plugin stopped.")


def on_reminder_finished(data):

    print(f"[Plugin Event] Reminder completed: {data['message']}")