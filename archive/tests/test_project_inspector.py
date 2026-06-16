from modules.automation.files import (
    list_files
)

from modules.automation.terminal import (
    run_terminal_command
)

print("\nFILES\n")
print(list_files())

print("\nPATH\n")
print(
    run_terminal_command(
        "pwd"
    )
)