import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider

from amazon.items import AmazonItem
from amazon.settings import DOMAIN_TO_SCRAPP,URL_TO_SEARCH,MAX_CANT_TO_SEARCH,URL_TO_SEARCH_WITH_ASIN
from scrapy import log

class AmazonSpiderItemWithAsin(CrawlSpider):
    name = 'amazon_with_asin'
    allowed_domain = [DOMAIN_TO_SCRAPP]
    start_urls = URL_TO_SEARCH_WITH_ASIN
    
    
    def parse(self, response):
        ml_item = AmazonItem()
        ml_item['ASIN'] = response.xpath('normalize-space(//th[contains(.,"ASIN")]//following-sibling::td/text())').extract()   ### .com 
       # ml_item['Title'] = response.xpath('normalize-space(//span[contains(@id,"productTitle")]/text())').extract()
       # ml_item['Description'] = response.xpath('normalize-space(//div[contains(@id,"productDescription")]/div/p[1]/text())').extract()
        ml_item['Price'] = response.xpath('normalize-space(//span[contains(@id,"priceblock_ourprice")]/text())').extract()
        ml_item['List_price'] = response.xpath('normalize-space(//span[contains(@class,"a-text-strike")]/text())').extract()
        #ml_item['Image_URL'] = response.xpath('normalize-space(//div[contains(@id,"imgTagWrapperId")]/img/@data-old-hires)').extract()
        yield ml_item
		
		
		###### AMAZON.COM #############
		
		#ml_item['ASIN'] = response.xpath('normalize-space(//th[contains(.,"ASIN")]//following-sibling::td/text())').extract()   ### .com 
		