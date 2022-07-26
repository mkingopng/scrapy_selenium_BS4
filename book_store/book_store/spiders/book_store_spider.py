# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookStoreSpiderSpider(CrawlSpider):
    name = 'book_store_spider'
    allowed_domains = ['books.toscrape.com']
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'

    def start_requests(self):
        yield scrapy.Request(url='http://books.toscrape.com/',
                             headers={'user_agent': self.user_agent})

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//article[@class='product_pod']/div/a"),
             callback='parse_item',
             follow=True,
             process_request='set_user_agent'),  # handle opening each book URL

        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a"),
             process_request='set_user_agent')  # handle pagination
    )

    def set_user_agent(self, request, spider):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            'book name': response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get(),
            'price': response.xpath("(//div[@class='col-sm-6 product_main']/p)[1]/text()").get()
        }
