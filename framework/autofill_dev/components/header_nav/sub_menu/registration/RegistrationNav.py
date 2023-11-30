from playwright.sync_api import Locator

from framework.autofill_dev.components.header_nav.sub_menu.NavBarSubMenu import NavBarSubmenu
from framework.autofill_dev.components.header_nav.sub_menu.registration.RegistrationSubMenuLinkTitles import \
    RegistrationSubMenuLinkTitles
from framework.autofill_dev.registration.email_and_username.EmailAndUsernamePage import EmailAndUsernamePage


class RegistrationNav(NavBarSubmenu):

    def __init__(self, toggle_locator: Locator):
        super().__init__(toggle_locator)

    def navigate_email_and_username(self):
        self.navigate_to(RegistrationSubMenuLinkTitles.EMAIL_AND_USERNAME)
        return EmailAndUsernamePage(self._toggleLocator.page)
