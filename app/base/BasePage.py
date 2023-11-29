from playwright.sync_api import Page


class BasePage:
    _page: Page

    def __init__(self, page: Page):
        self._page = page

