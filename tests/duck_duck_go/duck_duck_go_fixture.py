import pytest
from playwright.sync_api import Page

from app.duck_duck_go.search_page.DDGSearchPage import DDGSearchPage


@pytest.fixture
def duck_duck_go_page(page: Page):
    yield DDGSearchPage.open(page)
