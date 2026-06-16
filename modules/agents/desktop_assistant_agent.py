from modules.agents.screen_awareness_agent import (
    ScreenAwarenessAgent
)

from modules.agents.screen_understanding_agent import (
    ScreenUnderstandingAgent
)
from modules.agents.screen_change_detector import (
    ScreenChangeDetector
)
from modules.vision.window_context import (
    get_active_window
)

from modules.vision.window_analyzer import (
    analyze_window
)
from modules.memory.task_history import (
    TaskHistory
)

from modules.agents.task_inference_agent import (
    TaskInferenceAgent
)
from modules.memory.project_memory import (
    ProjectMemory
)
class DesktopAssistantAgent:

    def __init__(self):
        self.project_memory = (
            ProjectMemory()
        )
        self.task_inference = (
            TaskInferenceAgent()
        )

        self.task_history = (
            TaskHistory()
        )
        self.detector = (
            ScreenChangeDetector()
        )

        self.cached_result = None

        self.screen = (
            ScreenAwarenessAgent()
        )

        self.understanding = (
            ScreenUnderstandingAgent()
        )

    def observe(self):
        window = get_active_window()

        window_findings = []

        if window["success"]:

            window_findings = analyze_window(
                window["title"]
            )

        screen_result = (
            self.screen.observe()
        )

        if not screen_result["success"]:

            return screen_result

        image_path = "screen.png"

        if (
            not self.detector.has_changed(
                image_path
            )
            and
            self.cached_result
        ):

            print(
                "[Desktop] Using cache"
            )

            return self.cached_result

        summary = (
            self.understanding
            .understand(
                screen_result["raw_text"]
            )
        )
        task = (
            self.task_inference.infer(
                window_findings,
                screen_result["findings"],
                self.understanding
                    .get_recent_context()
            )
        )
        if "assistant" in task.lower():

            self.project_memory.add_fact(
                "AI Assistant",
                task
            )

        self.task_history.add(
            task
        )

        result = {

            "success": True,

            "summary": summary,

            "screen": screen_result,

            "task": task,

            "window": window,

            "window_findings": window_findings
        }

        self.cached_result = result

        return result

    def what_am_i_doing(self):

        result = self.observe()

        if not result["success"]:

            return result["error"]

        return result["summary"]

    def recent_activity(self):

        return (
            self.understanding
            .get_recent_context()
        )
    def current_task(self):

        return (
            self.task_history.latest()
        )
    def recent_tasks(self):

        return (
            self.task_history.recent()
        )
    def project_status(self):

        return (
            self.project_memory.get_project(
                "AI Assistant"
            )
        )