# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import string
import re
from netMusic.items import NetmusicItem


class MusiclistSpider(CrawlSpider):
    name = 'musicList'
    allowed_domains = ['music.163.com']
    start_urls = ['https://music.163.com/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=35']

    rules = (
        # 匹配初始页面的所有可点击到歌单的地址
        Rule(LinkExtractor(allow=r'/playlist\?id=\d+'), callback='parse_item',follow=True),
        Rule(LinkExtractor(restrict_xpaths=r'//div/a[@class="zbtn znxt"]/@href'),follow=True)
    )

    def parse_item(self, response):
        # 已经在middleware中切换iframe。
        # driver = response.meta['driver']
        # driver.switch_to.default_content()
        # g_iframe = driver.find_elements_by_tag_name('iframe')[0]
        # driver.switch_to.frame(g_iframe)

        print("............................................")
        # HTMLResponse 支持xpath和css以及re查找
        title = response.xpath(r'//span[@class="txt"]/a/b/@title').extract_first()
        duration = response.xpath(r'//tr/td[@class="s-fc3"]/span[@class="u-dur"]/text()').extract_first()
        singer = response.xpath(r'//tr/td[4]/div/span/@title').extract_first()
        album = response.xpath(r'//tr/td[5]/div[@class="text"]/a/@title').extract_first()
        item = NetmusicItem()


        item['title'] = title
        item['duration'] = duration
        item['singer'] = singer
        item['album'] = album

        print(item)
        yield item
