class ResponseAgent:

    def respond(self, result):

        if not result:
            return "I could not complete the task."

        if result.get("success"):

            if "output" in result:
                return result["output"]

            if "query" in result:
                return f"Search completed for {result['query']}"

            return "Task completed successfully."

        return result.get(
            "error",
            "Task failed."
        )