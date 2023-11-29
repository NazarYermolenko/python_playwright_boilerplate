import pytest

from app.duck_duck_go.DuckDuckGoPage import DuckDuckGoPage
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
        search_page: DuckDuckGoPage) -> None:
    search_page.search_for(phrase)

    WaitUtils.until((lambda: len(search_page.get_results()) > 0), True)

    results = search_page.get_results()

    for result in results:
        assert phrase.lower() in result.get_title().lower()
