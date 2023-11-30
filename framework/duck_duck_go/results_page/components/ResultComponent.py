from playwright.sync_api import Locator

from framework.base.BaseComponentWrapper import BaseComponentWrapper


class ResultComponent(BaseComponentWrapper):
    def _title_locator(self):
        return self._wrapLocator.locator("[data-testid='result-title-a']")

    def __init__(self, locator: Locator):
        super().__init__(locator)

    def get_title(self):
        return self._title_locator().text_content()