# -*- coding: utf-8 -*-
__author__ = 'admin'

from crawler import Crawler

crawler = Crawler()
print crawler.crawl('http://vk.com', ['http://vk.com'], 1)



