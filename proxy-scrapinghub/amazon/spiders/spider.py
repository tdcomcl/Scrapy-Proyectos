import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider

from amazon.items import AmazonItem
from amazon.settings import DOMAIN_TO_SCRAPP,URL_TO_SEARCH,MAX_CANT_TO_SEARCH
from scrapy import log


class AmazonSipder(CrawlSpider):
    name = 'amazon' 
    count_item_scrapp = 0
    allowed_domain = [DOMAIN_TO_SCRAPP]
    start_urls = [URL_TO_SEARCH]

    
    rules = {       
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[contains(@id,"pagnNextLink")]'))),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[contains(@class,"s-access-detail-page")]')),callback='parse_item',follow=False)
    }
    def parse_item(self, response):
        ml_item = AmazonItem()
        ml_item['ASIN'] = response.xpath('normalize-space(//th[contains(.,"ASIN")]//following-sibling::td/text())').extract()
        ml_item['Title'] = response.xpath('normalize-space(//span[contains(@id,"productTitle")]/text())').extract()
        ml_item['Description'] = response.xpath('normalize-space(//div[contains(@id,"productDescription")]/div/p[1]/text())').extract()
        ml_item['Price'] = response.xpath('normalize-space(//span[contains(@id,"priceblock_ourprice")]/text())').extract()
        ml_item['List_price'] = response.xpath('normalize-space(//span[contains(@class,"a-text-strike")]/text())').extract()
        ml_item['Image_URL'] = response.xpath('normalize-space(//div[contains(@id,"imgTagWrapperId")]/img/@data-old-hires)').extract()     
        
        self.count_item_scrapp += 1

        if self.count_item_scrapp > MAX_CANT_TO_SEARCH:
            raise CloseSpider('item_exceeded')
        yield ml_item