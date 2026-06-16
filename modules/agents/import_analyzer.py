from pathlib import Path


class ImportAnalyzer:


    def find_users(
        self,
        module_name
    ):

        results = []

        for file_path in Path(".").rglob("*.py"):

            try:

                content = file_path.read_text()

                if module_name in content:

                    results.append(
                        str(file_path)
                    )

            except Exception:

                pass

        return results