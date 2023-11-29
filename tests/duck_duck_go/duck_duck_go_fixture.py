import pytest
from playwright.sync_api import Page

from app.duck_duck_go.DuckDuckGoPage import DuckDuckGoPage


@pytest.fixture
def duck_duck_go_page(page: Page):
    yield DuckDuckGoPage.open(page)
