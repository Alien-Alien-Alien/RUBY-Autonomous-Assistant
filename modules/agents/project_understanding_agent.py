from modules.agents.architecture_agent import (
    ArchitectureAgent
)


class ProjectUnderstandingAgent:


    def analyze(self):

        architecture = (
            ArchitectureAgent()
        )

        data = (
            architecture.analyze()
        )

        return {

            "project_type":
                "AI Assistant",

            "python_files":

                data[
                    "project_summary"
                ][
                    "python_files"
                ],

            "total_lines":

                data[
                    "project_summary"
                ][
                    "total_lines"
                ],

            "major_components": [

                "Planning",

                "Execution",

                "Learning",

                "Memory",

                "Voice",

                "Automation"
            ]
        }