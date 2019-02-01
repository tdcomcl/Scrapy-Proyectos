# -*- coding: utf-8 -*-
import scrapy
from scrapy import signals
from scrapy.exporters import CsvItemExporter
from scrapy import Request
import csv


class AmazonPipeline(object):
    def __init__(self):
        self.files = {}
    
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline
		
    def spider_opened(self, spider):
        file = open('%s_items3.csv' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = CsvItemExporter(file)
        
        self.exporter.fields_to_export = [
            'ASIN',
            'Title',
            'Description',
            'Price',
            'List_price',
            'Image_URL'
        ]
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
