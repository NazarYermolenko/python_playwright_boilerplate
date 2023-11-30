import pytest
from playwright.sync_api import Browser

from framework.autofill_dev.main_page.AFMainPage import AFMainPage


@pytest.fixture
def autofill_fixture(base_fixture: Browser):
    yield AFMainPage.open(base_fixture.new_page())
