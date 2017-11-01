# -*- coding: utf-8 -*-
import scrapy


class XiciSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/s?wd=ip']

    def parse(self, response):
        print response.xpath('//span[@class="c-gap-right"]/text()').extract()[0]
