from playwright.sync_api import Page

from framework.base.BasePage import BasePage


class RegistrationResultsPage(BasePage):
    def _card_wrapper(self):
        return self._page.locator("//div[@class='card' and contains(., 'Form Submit Results')]")

    def _registration_result(self):
        return self._card_wrapper().locator('pre')

    def _back_button(self):
        return self._card_wrapper().locator('a').filter(has_text="Back")

    @property
    def header(self):
        from framework.autofill_dev.components.header_nav.AFHeaderNav import AFHeaderNav
        return AFHeaderNav(self._page)

    def __init__(self, page: Page):
        super().__init__(page)

    def get_registration_results(self):
        return self._registration_result().text_content()

    def navigate_back(self):
        self._back_button().click()

        from framework.autofill_dev.registration.email_and_username.EmailAndUsernamePage import EmailAndUsernamePage
        return EmailAndUsernamePage(self._page)
