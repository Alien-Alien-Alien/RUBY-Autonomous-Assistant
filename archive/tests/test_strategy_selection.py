from core.experience_memory import (
    success_rate
)

strategies = [

    {
        "name": "A",
        "successes": 5,
        "failures": 1
    },

    {
        "name": "B",
        "successes": 2,
        "failures": 4
    }
]

best = max(

    strategies,

    key=lambda s: success_rate(

        s["successes"],

        s["failures"]
    )
)

print(best)