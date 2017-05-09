# -*- coding: utf-8 -*-

import scrapy


class ReutersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    response_status = scrapy.Field()
    response_url = scrapy.Field()
    symbol = scrapy.Field()
    date = scrapy.Field()
