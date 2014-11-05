#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.support import wait
from helpers.page import Page
from selenium.webdriver.common.by import By
from unittest_data_provider import data_provider

class SeleniumTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.page = Page(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def setUp(self):
        self.page.open("http://2gis.ru")

    #def tearDown(self):
        #self.driver.close()
    
    def test_shareLink(self):
        oldSearchText = u'банк'
        self.page.search_bar.search(oldSearchText)
        oldResultsCount = self.page.search_result.count

        link = self.page.share_link().getLink()
        self.page.open(link)

        newSearchText = self.page.search_bar.getSearchText()
        newResultsCount = self.page.search_result.count
        self.assertEqual(oldSearchText, newSearchText, 'Search texts are not equal')
        self.assertEqual(oldResultsCount, newResultsCount, 'Result count differs: {} vs {}'.format(oldResultsCount, newResultsCount))

    def test_route(self):

        departuteText = u"карла маркса3444"
        destinationText = u"золотая нива44444"

        self.page.search_bar.searchPath(departuteText, destinationText)

        self.assertTrue(self.page.path_result().isFound(), 'Path was not found')
        #self.assertIsNot(self.page.path_result().foundSteps(), [], 'Path was not found')
   

    
    queries_for_searchBar = lambda: (
        (u'Банк', True),
        (u'Банк', True),
        (u'Школа', True),
        (u'йцукен', False),
        (u'абвдылг', False),
        (u'блдаж', False),
    )

    @data_provider(queries_for_searchBar)
    def test_searchBar(self, query, isCorrect):
        self.page.search_bar.search(query)
        self.assertEqual(self.page.search_result.count > 0, isCorrect, 'Wrong expected search result: {}'.format(self.page.search_result.count))
    

if __name__ == '__main__':
    unittest.main()
