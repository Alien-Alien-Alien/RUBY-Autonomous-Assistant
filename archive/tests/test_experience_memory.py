from core.experience_memory import (
    record_success,
    get_experience
)

record_success(

    "recover voice system",

    [
        "open firefox",

        "search troubleshooting"
    ]
)

print(

    get_experience(
        "recover voice system"
    )
)