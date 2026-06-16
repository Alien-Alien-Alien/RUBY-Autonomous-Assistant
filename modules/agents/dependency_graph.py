from pathlib import Path
import re


class DependencyGraph:


    def analyze(
        self,
        file_name
    ):

        path = Path(file_name)

        if not path.exists():

            return []

        content = path.read_text()

        imports = []

        imports = set()

        for line in content.splitlines():

            line = line.strip()

            if line.startswith("from "):

                parts = line.split()

                if len(parts) >= 2:

                    imports.add(
                        parts[1]
                    )

            elif line.startswith("import "):

                parts = line.split()

                if len(parts) >= 2:

                    imports.add(
                        parts[1]
                    )

        return sorted(
            list(imports)
        )