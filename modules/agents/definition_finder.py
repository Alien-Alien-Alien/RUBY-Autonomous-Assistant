from pathlib import Path


class DefinitionFinder:


    def find(
        self,
        function_name
    ):

        results = []

        search_text = (
            f"def {function_name}"
        )

        for file_path in Path(".").rglob("*.py"):

            try:

                content = (
                    file_path.read_text()
                )

                if search_text in content:

                    results.append(
                        str(file_path)
                    )

            except Exception:

                pass

        return results