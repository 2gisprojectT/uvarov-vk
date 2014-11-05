# -*- coding: utf-8 -*-

from helpers.base_component import BaseComponent
from selenium.webdriver.common.action_chains import ActionChains

class ButtonAddAttachment(BaseComponent):

    selectors = {
        'self': 'im_add_media_link',
        'add_photo': "document.querySelector('a[style*=\"attach_icons.png?6\"]').click();",
        'some_photo': '.photos_choose_row_bg',
        'some_photo_js': "document.querySelector('a[class^=photos_choose_row][class$=fl_l]').click();",
        'photos_choose_button': 'photos_choose_button'
    }

    def perform_mouse_over(self, element_to_hover_over):
        # = self.driver.find_element_by_id(self.selectors['self'])
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()

    # @return - src of an img
    def add_photo_attachment(self):
        # работает только с JS, т.к. кнопка скрыта, а при выборе после ховера она сразу исчезает
        self.driver.execute_script(self.selectors['add_photo'])
        img = self.driver.find_element_by_css_selector(self.selectors['some_photo'])
        src = img.value_of_css_property('src')
        img.click()
        #eturn src




