# -*- coding: utf-8 -*-

__author__ = 'admin'

from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SeleniumTest(TestCase):

    def test_search(self):
        driver = webdriver.Firefox()
        driver.get("http://www.2gis.ru/")
        driver.implicitly_wait(10)  # seconds
        elem = driver.find_element_by_class_name("suggest__input")
        elem.send_keys(u"Городdffdggdgfdffdfg")
        elem.send_keys(Keys.RETURN)
        not_found = False
        try:
            places = driver.find_element_by_class_name("mixedResults__geoTab")
        except:
            not_found = True
        self.assertFalse(not_found, "Нет результатов для запроса")

        places.click()
        assert u"Увы" not in driver.page_source
        driver.close()

if __name__ == '__main__':
    unittest.main()