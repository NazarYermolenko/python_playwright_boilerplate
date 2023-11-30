import pytest
from playwright.sync_api import Page, Browser

from framework.duck_duck_go.search_page.DDGSearchPage import DDGSearchPage


@pytest.fixture
def duck_duck_go_page(base_fixture: Browser):
    yield DDGSearchPage.open(base_fixture.new_page())
