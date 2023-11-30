from playwright.sync_api import Page, Locator

from framework.base.BasePage import BasePage


class EmailAndUsernamePage(BasePage):
    def _form_wrapper(self):
        return self._page.locator("form")

    def _email_input(self) -> Locator:
        return self._form_wrapper().locator("input[id='email']")

    def _username_input(self) -> Locator:
        return self._form_wrapper().locator("input[id='username']")

    def _password_input(self) -> Locator:
        return self._form_wrapper().locator("input[id='password']")

    def _confirm_password_input(self) -> Locator:
        return self._form_wrapper().locator("input[id='password-confirm']")

    def _register_button(self) -> Locator:
        return self._form_wrapper().locator("button[type='submit']")

    @property
    def header(self):
        from framework.autofill_dev.components.header_nav.AFHeaderNav import AFHeaderNav
        return AFHeaderNav(self._page)

    def __init__(self, page: Page):
        super().__init__(page)

    def set_email(self, text):
        self._email_input().clear()
        self._email_input().press_sequentially(text)
        return self

    def set_username(self, text):
        self._username_input().clear()
        self._username_input().press_sequentially(text)
        return self

    def set_password(self, text):
        self._password_input().clear()
        self._password_input().press_sequentially(text)
        return self

    def set_confirm_password(self, text):
        self._confirm_password_input().clear()
        self._confirm_password_input().press_sequentially(text)
        return self

    def register(self):
        self._register_button().click()
        from framework.autofill_dev.registration.RegistrationResultsPage import RegistrationResultsPage
        return RegistrationResultsPage(self._page)