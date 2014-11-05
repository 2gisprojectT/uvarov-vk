class ListOfDialogues():

    def __init__(self, driver):
        self.driver = driver
        self._dialogue_row = None

    @property
    def dialogue_row(self):
        from helpers.page_listOfDialogues_elements.dialogue_row import DialogueRow
        if self._dialogue_row is None:
            self._dialogue_row = DialogueRow(self.driver, self.driver.find_element_by_css_selector(DialogueRow.selectors['self']))
        return self._dialogue_row

    def open(self, url):
        self.driver.get(url)