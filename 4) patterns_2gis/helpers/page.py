class Page():
    def __init__(self, driver):

        self.driver = driver
        self._search_bar = None
        self._search_result = None
        self._close_button = None
        self._share_link = None
        self._path_result = None

    @property
    def search_bar(self):
        from helpers.search_bar import SearchBar

        if self._search_bar is None:
            self._search_bar = SearchBar(self.driver, self.driver.find_element_by_css_selector(SearchBar.selectors['self']))
        return self._search_bar

    @property
    def search_result(self):
        from helpers.search_result import SearchResult

        if self._search_result is None:
            self._search_result = SearchResult(self.driver, self.driver.find_element_by_css_selector(SearchResult.selectors['self']))
        return self._search_result

    #@property
    def share_link(self):
        from helpers.share_link import ShareLink
        if self._share_link is None:
            self._share_link = ShareLink(self.driver, self.driver.find_element_by_css_selector(ShareLink.selectors['self']))
        return self._share_link

    def path_result(self):
        from helpers.path_result import PathResult
        if self._path_result is None:
            self._path_result = PathResult(self.driver, self.driver.find_element_by_id(PathResult.selectors['self']))
        return self._path_result


    def open(self, url):
        self.driver.get(url)

