from playwright.sync_api import Locator


class BaseComponentWrapper:
    def __init__(self, locator: Locator):
        self._wrapLocator = locator
