from playwright.sync_api import Page, Response

from app.base.BasePage import BasePage
from app.duck_duck_go.components.ResultComponent import ResultComponent
from utils.url_provider.UrlProvider import UrlProvider


class DuckDuckGoPage(BasePage):
    def _search_input_locator(self):
        return self._page.locator("[id='searchbox_input']")

    def _results_locator(self):
        return self._page.locator("li[data-layout='organic']")

    def __init__(self, page: Page):
        super().__init__(page)

    @classmethod
    def open(cls, page: Page):
        url = UrlProvider.get_duck_duck_go_url()
        page.goto(url)
        return cls(page)

    def search_for(self, text: str):
        self._search_input_locator().clear()
        self._search_input_locator().press_sequentially(text)
        self._search_input_locator().press('Enter')

    def get_results(self) -> list[ResultComponent]:
        return [ResultComponent(locator) for locator in self._results_locator().all()]

