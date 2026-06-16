from modules.agents.context_agent import (
    ContextAgent
)

context = (

    ContextAgent()

    .build_context()
)

print(

    "\nCONTEXT\n"
)

print(context)

print(

    "\nSCREEN TEXT PREVIEW\n"
)

print(

    context["screen"]["text"][:300]
)