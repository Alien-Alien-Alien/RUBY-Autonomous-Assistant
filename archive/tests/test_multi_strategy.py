from core.experience_memory import (
    get_best_strategy,
    save_experiences
)

data = {

    "recover voice system": [

        {
            "strategy": [
                "open firefox",
                "search troubleshooting"
            ],

            "successes": 5,

            "failures": 1
        },

        {
            "strategy": [
                "restart plugin"
            ],

            "successes": 2,

            "failures": 4
        }
    ]
}

save_experiences(
    data
)

print(

    get_best_strategy(
        "recover voice system"
    )
)