import subprocess


def run_python_file(file_name):

    try:

        result = subprocess.run(

            ["python3", file_name],

            capture_output=True,

            text=True
        )

        success = (

            result.returncode == 0
        )

        return {

            "success": success,

            "stdout": result.stdout,

            "stderr": result.stderr
        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e)
        }