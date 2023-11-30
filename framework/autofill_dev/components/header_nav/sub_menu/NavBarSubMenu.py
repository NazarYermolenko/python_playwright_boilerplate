from enum import Enum

from playwright.sync_api import Locator

from framework.base.BaseComponentWrapper import BaseComponentWrapper


class NavBarSubmenu(BaseComponentWrapper):
    def __init__(self, toggle_locator: Locator):
        super().__init__(toggle_locator.page.locator("ul[class^='dropdown-menu']"))
        self._toggleLocator = toggle_locator
        self._is_opened = False
        self._links = self._wrapLocator.locator('a')

    def _open(self):
        if not self._is_opened:
            self._toggleLocator.click()
            self._is_opened = not self._is_opened

    def navigate_to(self, link_title: Enum):
        self._open()
        self._links.filter(has_text=link_title.value).first.click()
