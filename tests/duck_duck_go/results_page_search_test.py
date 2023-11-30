import pytest

from framework.duck_duck_go.results_page.DDGResultsPage import DDGResultsPage
from framework.duck_duck_go.search_page.DDGSearchPage import DDGSearchPage
from tests.duck_duck_go.data.SearchPhrasesProvider import SearchPhrasesProvider
from tests.duck_duck_go.duck_duck_go_fixture import duck_duck_go_page as search_page
from utils.wait_utils.WaitUtils import WaitUtils


@pytest.mark.parametrize('phrase', SearchPhrasesProvider.get_animals())
def test_results_page_search(
        phrase: str,
        search_page: DDGSearchPage) -> None:
    result_page = search_page.search_component.search_for("Phrase different from the needed to search on "
                                                          "results page")
    WaitUtils.until((lambda: len(result_page.get_results()) > 0))

    result_page.search_component.search_for(phrase)

    WaitUtils.until(lambda: get_results_count_which_contains_the_phrase(result_page, phrase) > 0)


def get_results_count_which_contains_the_phrase(result_page: DDGResultsPage, phrase: str) -> int:
    results = result_page.get_results()
    return len(list(filter(lambda result: phrase.lower() in result.get_title().lower(), results)))
