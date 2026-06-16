from modules.automation.apps import (
    open_firefox
)

import pyautogui

import time


class BrowserNavigationAgent:


    def _prepare_browser(self):

        open_firefox()

        time.sleep(3)


    def youtube_search(
        self,
        query
    ):

        self._prepare_browser()

        pyautogui.hotkey(
            "ctrl",
            "l"
        )

        time.sleep(0.5)

        pyautogui.write(
            f"https://www.youtube.com/results?search_query={query}",
            interval=0.02
        )

        pyautogui.press(
            "enter"
        )

        return {

            "success": True,

            "query": query
        }


    def google_search(
        self,
        query
    ):

        self._prepare_browser()

        pyautogui.hotkey(
            "ctrl",
            "l"
        )

        time.sleep(0.5)

        pyautogui.write(
            f"https://www.google.com/search?q={query}",
            interval=0.02
        )

        pyautogui.press(
            "enter"
        )

        return {

            "success": True,

            "query": query
        }


    def github_search(
        self,
        query
    ):

        self._prepare_browser()

        pyautogui.hotkey(
            "ctrl",
            "l"
        )

        time.sleep(0.5)

        pyautogui.write(
            f"https://github.com/search?q={query}",
            interval=0.02
        )

        pyautogui.press(
            "enter"
        )

        return {

            "success": True,

            "query": query
        }