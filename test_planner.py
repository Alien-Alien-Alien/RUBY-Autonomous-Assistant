from modules.agents.adaptive_planner import (
    AdaptivePlanner
)

planner = AdaptivePlanner()

tests = [

    "ask chatgpt what is robotics",

    "ask chatgpt who is elon musk",

    "open firefox and ask chatgpt what is robotics",

    "open firefox and go to github",

    "search youtube for robotics"
]

for test in tests:

    plan = planner.recover(test)

    print("\nINPUT:", test)

    print(plan.tasks)