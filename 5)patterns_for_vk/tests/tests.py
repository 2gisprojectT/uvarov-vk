# -*- coding: utf-8 -*-

from unittest import TestCase
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.page_dialogue import PageDialogue
from helpers.page_listOfDialogues import ListOfDialogues
from helpers.page_login import PageLogin

import string


# generation of a random string
def str_generator(size=6, chars=string.ascii_uppercase + string.digits):
    import random
    return ''.join(random.choice(chars) for _ in range(size))


class DialoguesTests(TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.pageDialogue = PageDialogue(cls.driver)
        cls.pageLogin = PageLogin(cls.driver)
        cls.pageListOfDialogues = ListOfDialogues(cls.driver)
        cls.pageLogin.open("http://www.vk.com/")
        cls.pageLogin.sign_up_with_test_credentials()
        WebDriverWait(cls.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".left_label.inl_bl")))



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def setUp(self):
        self.pageListOfDialogues.open("http://www.vk.com/im")
        self.pageListOfDialogues.dialogue_row.click()

    # tests
    def test_send_text_message(self):
        msg = str_generator(64)
        self.pageDialogue.send_text_message(msg)
        assert msg in self.pageDialogue.driver.page_source

    def test_send_message_with_attachment_photo(self):
        img_src = self.pageDialogue.button_add_attachment.add_photo_attachment()
        self.pageDialogue.send_text_message("image attachment")
        assert img_src in self.pageDialogue.driver.page_source

    def test_emoticons_in_message(self):
        self.pageDialogue.button_emoticons.add_some_emoticon()
        self.pageDialogue.send_text_message("Smile!")
        self.assertTrue(self.pageDialogue.isThereAnyEmoticons())


class LoginTests(TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.pageLogin = PageLogin(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def setUp(self):
        self.pageLogin.open("http://www.vk.com/")

    def tearDown(self):
        self.driver.find_element_by_id("logout_link").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "top_reg_link")))

    # tests
    def testLoginWithTelephone(self):
        self.pageLogin.login_field.enter_login("+79513609119")
        self.pageLogin.password_field.enter_password_and_confirm("test_password")
        self.assertTrue(len(self.driver.find_elements_by_css_selector(".left_label.inl_bl")) > 0)


    def testLoginWithEmail(self):
        self.pageLogin.login_field.enter_login("razoru@yandex.ru")
        self.pageLogin.password_field.enter_password_and_confirm("test_password")
        self.assertTrue(len(self.driver.find_elements_by_css_selector(".left_label.inl_bl")) > 0)

if __name__ == '__main__':
    unittest.main()
