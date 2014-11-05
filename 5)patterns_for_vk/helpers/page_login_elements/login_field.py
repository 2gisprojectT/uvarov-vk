from helpers.base_component import BaseComponent

class LoginField(BaseComponent):

    selectors = {
        'self': 'quick_email'
    }

    def enter_login(self, text):
        self.driver.find_element_by_id(self.selectors['self']).send_keys(text)
