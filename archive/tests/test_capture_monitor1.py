import mss

with mss.mss() as sct:

    monitor = sct.monitors[1]

    sct.grab(
        monitor
    )

    sct.shot(
        mon=1,
        output="temp/monitor1.png"
    )

print(
    "saved"
)