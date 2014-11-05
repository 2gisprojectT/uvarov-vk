from helpers.base_component import BaseComponent


class DialogueRow(BaseComponent):

    selectors = {
        'self': '.dialogs_row'
    }

    def click(self):
        self.driver.find_element_by_css_selector(self.selectors['self']).click()
