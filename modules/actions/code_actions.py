import subprocess


def run_python_file(filename):

    result = subprocess.run(
        ["python3", filename],
        capture_output=True,
        text=True
    )

    return (
        result.stdout
        +
        result.stderr
    )