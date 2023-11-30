from playwright.sync_api import Page

from app.base.BasePageElement import BasePageElement
from app.duck_duck_go.results_page.DDGResultsPage import DDGResultsPage


class SearchComponent(BasePageElement):
    def _search_input_locator(self):
        return self._page.locator("[id='searchbox_input']")

    def __init__(self, page: Page):
        super().__init__(page)

    def search_for(self, text: str):
        self._search_input_locator().clear()
        self._search_input_locator().press_sequentially(text)
        self._search_input_locator().press('Enter')

        return DDGResultsPage(self._page)