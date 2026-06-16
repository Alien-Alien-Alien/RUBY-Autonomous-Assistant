from modules.agents.context_agent import (
    ContextAgent
)


class PageUnderstandingAgent:


    def analyze(self):

        context = (

            ContextAgent()

            .build_context()
        )

        screen_text = (

            context["screen"]

            .get(
                "text",
                ""
            )

            .lower()
        )

        youtube_score = 0

        google_score = 0

        github_score = 0


        # -------------------------
        # YOUTUBE DETECTION
        # -------------------------

        if "youtube" in screen_text:

            youtube_score += 3

        if "subscribe" in screen_text:

            youtube_score += 1

        if "views" in screen_text:

            youtube_score += 1

        if "watch?v=" in screen_text:

            youtube_score += 2

        if "channel" in screen_text:

            youtube_score += 1


        # -------------------------
        # GOOGLE DETECTION
        # -------------------------

        if "google" in screen_text:

            google_score += 3

        if "google search" in screen_text:

            google_score += 2

        if "search google" in screen_text:

            google_score += 2

        if "images" in screen_text:

            google_score += 1

        if "maps" in screen_text:

            google_score += 1


        # -------------------------
        # GITHUB DETECTION
        # -------------------------

        if "github" in screen_text:

            github_score += 3

        if "repository" in screen_text:

            github_score += 1

        if "commit" in screen_text:

            github_score += 1

        if "pull request" in screen_text:

            github_score += 1

        if "issues" in screen_text:

            github_score += 1


        scores = {

            "youtube": youtube_score,

            "google": google_score,

            "github": github_score
        }


        page_type = max(

            scores,

            key=scores.get
        )


        if scores[page_type] == 0:

            page_type = "unknown"


        return {

            "success": True,

            "page_type": page_type,

            "scores": scores,

            "screen_text":

            screen_text[:300]
        }