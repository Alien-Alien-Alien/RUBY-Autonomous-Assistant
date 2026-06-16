from modules.agents.browser_agent import (
    BrowserAgent
)


class ResearchAgent:


    def search_topic(
        self,
        topic
    ):

        browser = BrowserAgent()

        return browser.search(
            topic
        )