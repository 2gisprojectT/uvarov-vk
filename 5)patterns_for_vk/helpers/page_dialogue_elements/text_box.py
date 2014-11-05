from helpers.base_component import BaseComponent
from selenium.webdriver.common.keys import Keys


class TextBox(BaseComponent):

    selectors = {
        'self': 'div[id^=im_editable]'
    }

    def send_keys(self, text):
        self.driver.find_element_by_css_selector(self.selectors['self']).send_keys(text)

    def send_text_message(self, msg):
        self.send_keys(msg)
        self.driver.find_element_by_css_selector(self.selectors['self']).send_keys(Keys.RETURN)

