from helpers.base_component import BaseComponent
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class SearchResult(BaseComponent):

    selectors = {
        'self': '.searchResults__list',
        'count': '//*[@id="module-1-9-1-1"]/nav/div[2]/div[2]',
        'mini_card': '.miniCard__content'
    }

    @property
    def count(self):
        """
        try:
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.selectors['count']))
        )
        return element.text
        """
        try:
            cnt = self.driver.find_elements_by_css_selector(self.selectors['mini_card']).count()
        except:
            cnt = 0
        return cnt