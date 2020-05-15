# -*- coding: utf-8 -*-
import scrapy
from ..items import ArtItem


class ArtspiderSpider(scrapy.Spider):
    name = 'artspider'
    allowed_domains = ['artlinkart.com']
    start_urls = ['http://artlinkart.com/cn/exhibition/schedule/2020/01']

    def parse(self, response):
        art_list = response.xpath('//div[@class="subnav"]//tr')
        for i_item in art_list:
            href = i_item.xpath(".//th/a/@href").extract_first()
            if type(href) == str:
                yield scrapy.Request('http://artlinkart.com' + href, callback=self.parse_detail)

        year = ['2020', '2019', '2018', '2017']
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        for a in year:
            for b in month:
                yield scrapy.Request('http://artlinkart.com/cn/exhibition/schedule/' + str(a) + '/' + str(b),
                                     callback=self.parse)

    def parse_detail(self, response):
        art_item = ArtItem(name="", date="", exhibition="", curator="", artist="")
        # title = i_item.xpath('.//tr[1]/th/text()').extract()
        # print(title)
        art_item['name'] = response.xpath('//div[@class="m1"]//div[@class="font_justify"]//h2/text()').extract_first()
        contant = response.xpath('.//div[@class="font_justify"]//tr')
        for it in contant:
            title = it.xpath('.//th/text()').extract_first().strip()
            if title == "展览日期":
                art_item['date'] = it.xpath('.//td/text()').extract_first()
            elif title == "展览馆":
                art_item['exhibition'] = it.xpath('.//td/a/text()').extract_first()
            elif title == "策展人":
                art_item['curator'] = it.xpath('.//td/a/text()').extract_first()
            elif title == "艺术家":
                art_item['artist'] = ','.join(it.xpath('.//td/a'))
        yield art_item

# custom_settings = {'ArtPipeline': {'art.pipelines.ArtPipeline': 300} }
