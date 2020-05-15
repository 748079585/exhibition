# -*- coding: utf-8 -*-
import scrapy
from ..items import Art2Item


class Art2spiderSpider(scrapy.Spider):
    name = 'art2spider'
    allowed_domains = ['exhibit.artron.net']
    start_urls = ['http://exhibit.artron.net/exhibition']

    def parse(self, response):
        art_list = response.xpath('//div[@class="exList"]//dl')
        for i_item in art_list:
            href = i_item.xpath(".//dt/a/@href").extract_first()
            if type(href) == str:
                yield scrapy.Request('http://exhibit.artron.net' + href, callback=self.parse_detail)

        next_link = response.xpath("//div[@class='listJump mt1']/a[last()]/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request('http://exhibit.artron.net' + str(next_link), callback=self.parse)
            # 一个是我们又获得的url，扔给引擎

    def parse_detail(self, response):
        art_item = Art2Item(name="", date="", time="", exhibition="", curator="", address="")
        art_item["name"] = response.xpath('//div[@class="pw fix exDetail artAdvBox"]//h1/text()').extract_first()
        info_list = response.xpath('.//div[@class="exInfo"]//dl')
        for i_item in info_list:
            title = i_item.xpath('.//dt/text()').extract_first()
            if title == "展览时间：":
                art_item['date'] = i_item.xpath('.//dd/text()').extract_first()
            elif title == "展览地址：":
                art_item['address'] = i_item.xpath('.//dd/text()').extract_first()
            elif title == "开幕时间：":
                art_item['time'] = i_item.xpath('.//dd/text()').extract_first()
            elif title == "展览机构：":
                art_item['exhibition'] = i_item.xpath('.//dd/a/text()').extract_first()
            elif title == "参展人员：":
                art_item['curator'] = i_item.xpath('.//dd/span/b/text()').extract_first()
        yield art_item

# custom_settings = {'ArtPipeline': {'art.pipelines.Art2Pipeline': 300} }
