from modules.agents.project_inspector import (
    ProjectInspector
)

from modules.agents.dependency_graph import (
    DependencyGraph
)


class ArchitectureAgent:


    def analyze(self):

        inspector = ProjectInspector()

        graph = DependencyGraph()

        summary = inspector.summarize()

        execution_dependencies = graph.analyze(

            "modules/agents/execution_agent.py"
        )

        return {

            "project_summary": summary,

            "execution_agent_dependencies":

                execution_dependencies
        }