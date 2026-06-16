from datetime import datetime
from configs.settings import LOG_FILE


def log_action(action):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_message = f"[{timestamp}] {action}\n"

    with open(LOG_FILE, "a") as file:

        file.write(log_message)


def log_error(error):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_message = f"[{timestamp}] ERROR: {error}\n"

    with open(LOG_FILE, "a") as file:

        file.write(log_message)