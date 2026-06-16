class ActionSelectorAgent:

    def choose_action(
        self,
        goal,
        page_type
    ):

        goal = goal.lower()

        if page_type == "youtube":

            if "search" in goal:

                query = (

                    goal
                    .replace(
                        "search",
                        ""
                    )
                    .strip()
                )

                return {

                    "success": True,

                    "action":
                    "youtube_search",

                    "query":
                    query
                }

        if page_type == "google":

            if "search" in goal:

                query = (

                    goal
                    .replace(
                        "search",
                        ""
                    )
                    .strip()
                )

                return {

                    "success": True,

                    "action":
                    "google_search",

                    "query":
                    query
                }

        if page_type == "github":

            if "search" in goal:

                query = (

                    goal
                    .replace(
                        "search",
                        ""
                    )
                    .strip()
                )

                return {

                    "success": True,

                    "action":
                    "github_search",

                    "query":
                    query
                }

        return {

            "success": False,

            "action":
            None
        }