from helpers.base_component import BaseComponent


class SearchBar(BaseComponent):

    selectors = {
        'self': '.online__searchBar',
        'input': '.searchBar__form .searchBar__textfield._refbook .suggest__input',
        'from': '.searchBar__form .searchBar__textfield._from .suggest__input',
        'to':   '.searchBar__form .searchBar__textfield._to .suggest__input',
        'submit': '.searchBar__submit._refbook',
        'submit_path': '.searchBar__submit._rs',
        'route_tab': '.searchBar__tab.searchBar__rsTab',
        'search_tab': '.searchBar__tab.searchBar__refbookTab'
    }

    def search(self, query):
        self.driver.find_element_by_css_selector(self.selectors['search_tab']).click()
        self.driver.find_element_by_css_selector(self.selectors['input']).send_keys(query)
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit()

    def getSearchText(self):
        return self.driver.find_element_by_css_selector(self.selectors['input']).get_attribute('value')

    def searchPath(self, departute, destination):
        self.driver.find_element_by_css_selector(self.selectors['route_tab']).click()
        self.driver.find_element_by_css_selector(self.selectors['from']).send_keys(departute)
        self.driver.find_element_by_css_selector(self.selectors['to']).send_keys(destination)
        self.driver.find_element_by_css_selector(self.selectors['submit_path']).submit()

