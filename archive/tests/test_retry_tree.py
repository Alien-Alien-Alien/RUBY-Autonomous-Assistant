from modules.behavior_tree.action_node import ActionNode

from modules.behavior_tree.retry_decorator import RetryDecorator


counter = 0


def unstable_action():

    global counter

    counter += 1


    print(

        f"Attempt {counter}"
    )


    if counter < 3:

        raise Exception(

            "Temporary failure"
        )


    print("Action succeeded.")


tree = RetryDecorator(

    ActionNode(

        unstable_action
    ),

    retries=5
)


result = tree.run()

print(

    "Tree Success:",

    result
)