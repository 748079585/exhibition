# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy_djangoitem import DjangoItem
from app1.models import ArtItem, Art2Item, Art3Item


class ArtItem(DjangoItem):
    django_model = ArtItem


class Art2Item(DjangoItem):
    django_model = Art2Item


class Art3Item(DjangoItem):
    django_model = Art3Item


class ArtIItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    artist = scrapy.Field()
    curator = scrapy.Field()
    address = scrapy.Field()
    exhibition = scrapy.Field()
