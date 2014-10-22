#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.support import wait
from helpers.page import Page
from selenium.webdriver.common.by import By

class SeleniumTest(TestCase):

    def test_shareLink(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        page = Page(driver)
        page.open("http://2gis.ru")
        oldSearchText = u'банк'
        page.search_bar.search(oldSearchText)
        oldResultsCount = page.search_result.count

        link = page.share_link().getLink()
        page.open(link)

        newSearchText = page.search_bar.getSearchText()
        newResultsCount = page.search_result.count
        self.assertEqual(oldSearchText, newSearchText, 'Search texts are not equal')
        self.assertEqual(oldResultsCount, newResultsCount, 'Result count differs')
        driver.close()

    def test_route(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        page = Page(driver)
        page.open("http://2gis.ru")

        departuteText = u"карла маркса"
        destinationText = u"золотая нива"

        page.search_bar.searchPath(departuteText, destinationText)

        self.assertTrue(page.path_result().isFound(), 'Path was not found')
        driver.close()


if __name__ == '__main__':
    unittest.main()
