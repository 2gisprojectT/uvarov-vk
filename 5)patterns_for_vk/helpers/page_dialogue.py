# -*- coding: utf-8 -*-
class PageDialogue():

    selectors = {
        'emoticon': 'img[class=emoji_css][alt]'
    }

    def __init__(self, driver):
        self.driver = driver
        self._text_box = None
        self._button_add_attachment = None
        self._button_emoticons = None

    @property
    def text_box(self):
        from helpers.page_dialogue_elements.text_box import TextBox
        if self._text_box is None:
            self._text_box = TextBox(self.driver, self.driver.find_element_by_css_selector(TextBox.selectors['self']))
        return self._text_box

    @property
    def button_add_attachment(self):
        from helpers.page_dialogue_elements.button_add_attachment import ButtonAddAttachment
        if self._button_add_attachment is None:
            self._button_add_attachment = ButtonAddAttachment(self.driver, self.driver.find_element_by_id(ButtonAddAttachment.selectors['self']))
        return self._button_add_attachment

    @property
    def button_emoticons(self):
        from helpers.page_dialogue_elements.button_emoticons import ButtonEmoticons
        from helpers.page_dialogue_elements.button_emoticons import get_first_non_hidden_element
        if self._button_emoticons is None:
            self._button_emoticons = ButtonEmoticons(self.driver, get_first_non_hidden_element(self.driver, ButtonEmoticons.selectors['self']))
        return self._button_emoticons

    def open(self, url):
        self.driver.get(url)

    def send_text_message(self, msg):
        self.text_box.send_text_message(msg)

    def isThereAnyEmoticons(self):
        return len(self.driver.find_elements_by_css_selector(self.selectors['emoticon'])) > 0