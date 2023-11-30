import pytest
from playwright.sync_api import Page

from framework.autofill_dev.main_page.AFMainPage import AFMainPage


@pytest.fixture
def autofill_fixture(page: Page):
    yield AFMainPage.open(page)
