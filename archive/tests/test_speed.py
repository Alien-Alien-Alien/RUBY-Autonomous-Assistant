import time

from modules.voice.tts import (
    speak
)

start = time.time()

speak(
    "Hello Ahilan, this is a speed test."
)

end = time.time()

print(
    round(
        end - start,
        2
    ),
    "seconds"
)