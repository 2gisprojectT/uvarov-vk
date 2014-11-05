from helpers.base_component import BaseComponent
from selenium.webdriver.common.keys import Keys


class PasswordField(BaseComponent):

    selectors = {
        'self': 'quick_pass'
    }

    def enter_password(self, text):
        self.driver.find_element_by_id(self.selectors['self']).send_keys(text)

    def enter_password_and_confirm(self, password):
        self.enter_password(password)
        self.enter_password(Keys.ENTER)


