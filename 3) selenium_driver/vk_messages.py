# -*- coding: utf-8 -*-

__author__ = 'admin'

from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


import string
import random
# генерация случайной строки
def str_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class TestSendTextMessage(unittest.TestCase):
    #precondition: logged in
    def test_attach_photo(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)  # seconds
        driver.get("http://www.vk.com/")
        login = driver.find_element_by_id("quick_email")
        login.send_keys("+79513609119")
        password = driver.find_element_by_id("quick_pass")
        password.send_keys("test_password")
        password.send_keys(Keys.RETURN)

        msg_button = driver.find_element_by_id("l_msg")
        action = webdriver.ActionChains(driver)
        msg_button.click()
        write_msg_button = driver.find_element_by_id("im_write_btn")
        write_msg_button.click()
        drop_down_addressee = driver.find_element_by_id("imw_inp")
        drop_down_addressee.click()
        drop_down_addressee.send_keys(Keys.RETURN)

        text_edit = driver.find_element_by_class_name("im_editable")
        msg = str_generator(50)
        text_edit.send_keys(msg)
        send_button = driver.find_element_by_id("imw_send")
        send_button.click()
        #body_text = driver.find_elements_by_css_selector(".im_msg_text")
        #self.assertTrue("Text not found!", bodyText.contains(msg));
        assert msg in driver.page_source


if __name__ == '__main__':
    unittest.main()
