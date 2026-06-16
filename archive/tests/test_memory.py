from modules.memory.long_term_memory import (

    remember,

    recall,

    load_memory
)


load_memory()


remember(

    "favorite_topic",

    "robotics"
)


print(

    recall("favorite_topic")
)