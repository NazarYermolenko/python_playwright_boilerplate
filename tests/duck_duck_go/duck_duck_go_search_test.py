import pytest

from framework.duck_duck_go.search_page.DDGSearchPage import DDGSearchPage
from tests.duck_duck_go.data.SearchPhrasesProvider import SearchPhrasesProvider
from tests.duck_duck_go.duck_duck_go_fixture import duck_duck_go_page as search_page
from utils.wait_utils.WaitUtils import WaitUtils


@pytest.mark.parametrize('phrase', SearchPhrasesProvider.get_animals())
def test_basic_duckduckgo_search(
        phrase: str,
        search_page: DDGSearchPage) -> None:
    result_page = search_page.search_component.search_for(phrase)

    WaitUtils.until((lambda: len(result_page.get_results()) > 0))

    results = result_page.get_results()
    for result in results:
        assert phrase.lower() in result.get_title().lower()
