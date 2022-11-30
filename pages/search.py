from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoSearchPage:

    URL = 'https://www.duckduckgo.com'
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')
    SEARCH_BUTTON = (By.ID, 'search_button_homepage')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        
        # submit search via ENTER
        # search_input.send_keys(phrase + Keys.RETURN)

        # submit search via clicking "Search"
        search_input.send_keys(phrase)
        search_button.click()
        