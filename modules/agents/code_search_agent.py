from pathlib import Path


class CodeSearchAgent:


    def search(
        self,
        keyword
    ):

        results = []

        for file_path in Path(".").rglob("*.py"):

            try:

                content = file_path.read_text()

                if keyword in content:

                    results.append(
                        str(file_path)
                    )

            except Exception:

                pass

        return results