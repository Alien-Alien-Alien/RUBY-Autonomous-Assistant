from modules.plugins.voice_plugin import (
    initialize
)

from core.capability_registry import (
    show_capabilities
)

print("BEFORE:")
print(show_capabilities())

initialize()

print("AFTER:")
print(show_capabilities())