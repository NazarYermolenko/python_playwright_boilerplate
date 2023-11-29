from playwright.sync_api import Locator


class BaseComponentWrapper:
    wrapLocator: Locator

    def __init__(self, locator: Locator):
        self.wrapLocator = locator
