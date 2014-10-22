from helpers.base_component import BaseComponent

class ShareLink(BaseComponent):

    selectors = {
        'self': '.extras__share',
        'url': '.share__popupUrlInput'
    }

    def click(self):
        self.driver.find_element_by_css_selector(self.selectors['self']).click()

    def getLink(self):
        self.click()
        return self.driver.find_element_by_css_selector(self.selectors['url']).get_attribute('value')

