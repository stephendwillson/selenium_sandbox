import pytest

from pages.results import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

@pytest.mark.parametrize('search_term', ['carl sagan', 'manningface', 'red panda'])
def test_basic_duckduckgo_search(browser, search_term):

    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    search_page.load()

    search_page.search(search_term)

    # validate title and search input match specified term
    assert search_term in result_page.title()
    assert search_term == result_page.search_input_value()
    
    # validate search input shows up in results
    for title in result_page.result_link_titles():
        assert search_term.lower() in title.lower()