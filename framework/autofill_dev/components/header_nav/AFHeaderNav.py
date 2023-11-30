from playwright.sync_api import Page

from framework.autofill_dev.components.header_nav.sub_menu.registration.RegistrationNav import RegistrationNav
from framework.base.BasePageElement import BasePageElement


class AFHeaderNav(BasePageElement):
    @property
    def registration(self):
        return RegistrationNav(self._page.locator("//a[contains(., 'Registration')]"))

    def __init__(self, page: Page):
        super().__init__(page)
        self._locator = self._page.locator("nav")
        self._is_opened = False
