# -*- coding: utf-8 -*-
# Basic Crawl spider
from scrapy.spiders import CrawlSpider, Rule

from scrapy.linkextractors import LinkExtractor
class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    allowed = 'travel'
    rules = (Rule(LinkExtractor(allow=(allowed)), callback='parse_page', follow=False),)

    def parse_page(self, response):
        a = response.xpath('//h3/a/@title').extract()

        l = 0
        for i in a:
            if l < len(i):
                l = len(i)

        print()
        print(self.allowed.capitalize(), 'Book Titles')
        print('-'*l)
        for i in a:
            print(i)
        print()
