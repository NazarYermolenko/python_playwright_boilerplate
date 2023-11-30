import pytest

from app.duck_duck_go.search_page.DDGSearchPage import DDGSearchPage
from tests.duck_duck_go.duck_duck_go_fixture import duck_duck_go_page as search_page
from utils.wait_utils.WaitUtils import WaitUtils

ANIMALS = [
    'panda',
    'python',
    'polar bear',
    'parrot',
    'porcupine',
    'parakeet',
    'pangolin',
    'panther',
    'platypus',
    'peacock'
]


@pytest.mark.parametrize('phrase', ANIMALS)
def test_basic_duckduckgo_search(
        phrase: str,
        search_page: DDGSearchPage) -> None:
    result_page = search_page.get_search_component().search_for(phrase)

    WaitUtils.until((lambda: len(result_page.get_results()) > 0))

    results = result_page.get_results()
    for result in results:
        assert phrase.lower() in result.get_title().lower()
