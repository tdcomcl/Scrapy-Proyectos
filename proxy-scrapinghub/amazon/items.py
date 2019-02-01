# -*- coding: utf-8 -*-
import scrapy

class AmazonItem(scrapy.Item):
    ASIN = scrapy.Field()
    Title = scrapy.Field()
    Description = scrapy.Field()
    Price = scrapy.Field()
    List_price = scrapy.Field()
    Image_URL = scrapy.Field()