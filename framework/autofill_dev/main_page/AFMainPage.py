from playwright.sync_api import Page

from framework.autofill_dev.components.header_nav.AFHeaderNav import AFHeaderNav
from framework.base.BasePage import BasePage
from utils.url_provider.UrlProvider import UrlProvider


class AFMainPage(BasePage):
    @property
    def header(self):
        return AFHeaderNav(self._page)

    def __init__(self, page: Page):
        super().__init__(page)

    @classmethod
    def open(cls, page: Page):
        url = UrlProvider.get_autofill_url()
        page.goto(url)
        return cls(page)
