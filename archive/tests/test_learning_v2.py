from core.experience_memory import (
    record_success,
    get_best_strategy
)

record_success(

    "recover voice system",

    [
        "open firefox",
        "search troubleshooting"
    ]
)

record_success(

    "recover voice system",

    [
        "restart plugin"
    ]
)

record_success(

    "recover voice system",

    [
        "open firefox",
        "search troubleshooting"
    ]
)

print(

    get_best_strategy(
        "recover voice system"
    )
)