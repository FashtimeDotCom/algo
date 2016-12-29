# coding: utf-8

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    html = scrapy.Field()
