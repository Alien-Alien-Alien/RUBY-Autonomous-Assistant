from modules.automation.files import (
    list_files,
    read_file
)


class ProjectInspector:


    def inspect(self):

        files = list_files()

        summary = []

        if not files["success"]:

            return files

        for name in files["files"][:10]:

            if name.endswith(".py"):

                result = read_file(name)

                if result["success"]:

                    summary.append({

                        "file": name,

                        "size": len(
                            result["content"]
                        ),

                        "lines": len(
                            result["content"].splitlines()
                        )
                    })

        return summary

    def summarize(self):

        files = list_files()

        if not files["success"]:

            return files

        python_files = 0

        total_lines = 0

        largest_file = None

        largest_size = 0

        for name in files["files"]:

            if not name.endswith(".py"):

                continue

            result = read_file(name)

            if not result["success"]:

                continue

            content = result["content"]

            size = len(content)

            lines = len(content.splitlines())

            python_files += 1

            total_lines += lines

            if size > largest_size:

                largest_size = size

                largest_file = name

        return {

            "python_files": python_files,

            "total_lines": total_lines,

            "largest_file": largest_file,

            "largest_size": largest_size
        }