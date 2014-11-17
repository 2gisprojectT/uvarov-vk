# -*- coding: utf-8 -*-
__author__ = 'admin'

import requests
import lxml.html
from tidylib import tidy_document


class Crawler:

    def is_url_available(self, url):
        try:
            r = requests.get(url)
            if r.status_code != requests.codes.ok:
                return False
        except:
            return False
        return True

    def is_html_valid(self, page):
        return True

    def is_css_valid(self, css):
        return True

    def find_all_urls_on_page(self, page_url):
        urls = []
        r = requests.get(page_url)
        dom = lxml.html.fromstring(r.text)
        dom.make_links_absolute(page_url, True)
        for link in dom.xpath('//a/@href'):
            urls.append(link)
        return urls

    def url_domain_is_allowed(self, url, allowed_urls):
        return True
        #return url in allowed_urls

    """
    @ starting_url - url, с которого начинается поиск - string
    @ allowed_urls - список url, которые принадлежат нашему сервису - list_of_strings
    @ max_depth - максимальная глубина поиска (-1 значит без ограничения) - int
    @ return - {bad_urls, bad_htmls, bad_css}
        @ return.bad_urls - {page_url, url} - список битых ссылок (страница и битая ссылка)
        @ return.bad_htmls {page_url} - список невалидных html страниц
        @ return.bad_csses {page_url, css_url} - список невалидных таблиц стилей
    """
    def crawl(self, starting_url, allowed_urls, max_depth):
        if not self.is_url_available(starting_url):
            raise ValueError('Starting page is not available')
        bad_urls = []
        bad_htmls = []
        bad_csses = []
        urls_to_attend = [[starting_url, 0]]
        visited = []
        while len(urls_to_attend) > 0:
            cur_url, cur_depth = urls_to_attend.pop()                       # достанем последний url и глубину
            print cur_url
            if max_depth != -1 and cur_depth > max_depth:                   # если глубина достигнута,
                continue                                                    # не будем рассматривать данный url;
            if not self.is_html_valid(url):                                 # найдем ошибки в html
                bad_htmls.append(url)                                       # добавим в список невалидных html
                print 'NON-VALID HTML: ' + cur_url
            all_urls_on_page = self.find_all_urls_on_page(cur_url)          # найдем все ссылки на странице
            for url in all_urls_on_page:                                    # для каждой ссылки
                if self.is_url_available(url):                              # если доступна
                    if self.url_domain_is_allowed(url, allowed_urls):       # если ее домен разрешен для посешения
                        if not url in visited:                              # если она еще не посещена
                            urls_to_attend.append([url, cur_depth+1])       # добавим в стек
                            visited.append(url)                             # добавим в список посещенных
                else:                                                       # если недоступна
                    bad_urls.append([cur_url, url])                         # добавим в список битых ссылок
                    print 'FAULT URL: ' + url + ' on ' + cur_url            #
                if not self.is_css_valid(url):                              # если css не валиден
                    bad_csses.append(url)                                   # добавим в список битых css
        return bad_urls, bad_htmls, bad_csses
