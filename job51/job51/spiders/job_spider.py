# -*- coding: utf-8 -*-
import scrapy


class JobSpiderSpider(scrapy.Spider):
    name = 'job_spider'
    allowed_domains = ['https://www.51job.com/']
    start_urls = ['http://https://www.51job.com//']

    def parse(self, response):
        pass
