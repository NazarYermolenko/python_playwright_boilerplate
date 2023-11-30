from playwright.sync_api import Page


class BasePageElement:
    def __init__(self, page: Page):
        self._page = page