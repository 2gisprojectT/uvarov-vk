from helpers.base_component import BaseComponent
from selenium.webdriver.common.keys import Keys

def get_first_non_hidden_element(driver, selector):
        elems = driver.find_elements_by_css_selector(selector)
        ans = None
        for elem in elems:
            if(elem.is_displayed()):
                ans = elem
                break
        return ans

class ButtonEmoticons(BaseComponent):

    selectors = {
        'self': '.emoji_smile.fl_l',
        'some_emoticon': '.emoji_smile_cont.emoji_smile_shadow'
    }

    def click(self):
        get_first_non_hidden_element(self.driver, self.selectors['self']).click()

    def add_some_emoticon(self):
        self.click()
        get_first_non_hidden_element(self.driver, self.selectors['some_emoticon']).click()

