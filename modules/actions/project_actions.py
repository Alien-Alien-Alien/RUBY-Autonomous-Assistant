import os


def create_python_project(name):

    os.makedirs(
        name,
        exist_ok=True
    )

    open(
        f"{name}/main.py",
        "w"
    ).close()

    open(
        f"{name}/README.md",
        "w"
    ).close()

    open(
        f"{name}/requirements.txt",
        "w"
    ).close()

    return (
        f"Created project {name}"
    )
