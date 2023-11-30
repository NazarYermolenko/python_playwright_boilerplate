from playwright.sync_api import Page

from framework.base.BasePage import BasePage
from framework.duck_duck_go.components.SearchComponent import SearchComponent
from framework.duck_duck_go.results_page.components.ResultComponent import ResultComponent


class DDGResultsPage(BasePage):
    @property
    def search_component(self):
        return SearchComponent(self._page)

    def _results_locator(self):
        return self._page.locator("li[data-layout='organic']")

    def __init__(self, page: Page):
        super().__init__(page)

    def get_results(self) -> list[ResultComponent]:
        return [ResultComponent(locator) for locator in self._results_locator().all()]
