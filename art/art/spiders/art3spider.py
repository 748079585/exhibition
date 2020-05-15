# -*- coding: utf-8 -*-
import scrapy
from ..items import Art3Item
from selenium import webdriver
from selenium.webdriver import ChromeOptions


class Art3spiderSpider(scrapy.Spider):
    name = 'art3spider'
    allowed_domains = ['exhibit.99ys.com']
    start_urls = ['http://exhibit.99ys.com/qbzl']

    def __init__(self):
        # 在初始化淘宝对象时，创建driver
        super(Art3spiderSpider, self).__init__(name='art3spider')
        option = ChromeOptions()
        option.headless = True
        self.driver = webdriver.Chrome(r"/Users/krystal/pythonWokespace/chromedriver", chrome_options=option)

    def parse(self, response):
        art_list = response.xpath('//div[@class="zl_display_block"]//div[@class="zl_xh"]')
        for i_item in art_list:
            art_item = Art3Item(name="", date="", time="", artist="", curator="", address="")
            contant = i_item.xpath('.//div[@class="zl_xq"]')
            for it in contant:
                art_item['name'] = it.xpath('.//div[@class="zl_mc"]/a/text()').extract_first()
                ul = it.xpath('.//ul//li')
                for li in ul:
                    title = li.xpath('.//text()').extract_first().strip()
                    if title.find("展览时间") >= 0:
                        art_item['date'] = li.xpath('.//span/text()').extract_first()
                    elif title.find("开幕时间") >= 0:
                        art_item['time'] = li.xpath('.//text()').extract_first().split('：')[1]
                    elif title.find("艺术家") >= 0:
                        artist = ','.join(li.xpath('.//a/text()').extract())
                        art_item['artist'] = artist[0:254]
                    elif title.find("策展人") >= 0:
                        art_item['curator'] = li.xpath('.//a/text()').extract_first()
                    elif title.find("展览地点") >= 0:
                        art_item['address'] = li.xpath('.//text()').extract_first().split('：')[1]
            yield art_item

        # next_link = response.xpath("//div[@class='fy']/a[@class='xyy']/@href").extract()
        # print('next_link:' + next_link[0])
        # if next_link:
        #     next_link = next_link[0]
        #     yield scrapy.Request(next_link, callback=self.parse)
            # 一个是我们又获得的url，扔给引擎
