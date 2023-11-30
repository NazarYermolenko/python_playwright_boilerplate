from playwright.sync_api import Page

from app.base.BasePage import BasePage
from app.duck_duck_go.components.SearchComponent import SearchComponent
from utils.url_provider.UrlProvider import UrlProvider


class DDGSearchPage(BasePage):

    def get_search_component(self):
        return SearchComponent(self._page)

    def __init__(self, page: Page):
        super().__init__(page)

    @classmethod
    def open(cls, page: Page):
        url = UrlProvider.get_duck_duck_go_url()
        page.goto(url)
        return cls(page)
