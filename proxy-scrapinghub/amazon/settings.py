# -*- coding: utf-8 -*-
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware

BOT_NAME = 'amazon'

DEFAULT_REQUEST_HEADERS = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                           'accept-encoding': 'gzip, deflate, sdch',
                           'accept-language': 'en-US,en;q=0.8',
                           'upgrade-insecure-requests': '1',
                           'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3'}


# Retry many times since proxies often fail
RETRY_TIMES = 5
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]


SPIDER_MODULES = ['amazon.spiders']
NEWSPIDER_MODULE = 'amazon.spiders'

# Configuración
# Dominio a scrapp.
DOMAIN_TO_SCRAPP = "https://www.amazon.com/"

# url con la búsqueda ( lego, impresoras, etc )
#URL_TO_SEARCH = "https://www.amazon.com/s/s/ref=sr_nr_p_85_0?fst=as%3Aoff&rh=n%3A165793011%2Ck%3Afunko+pop%2Cp_85%3A2470955011&keywords=funko+pop&ie=UTF8&qid=1548609620&rnid=2470954011"

#
URL_TO_SEARCH = "https://www.amazon.com/gp/product/B00ATABRJE"
#URL_TO_SEARCH =  []

#f = open("/home/ubuntu/arana-amazon/proxy-scrapinghub/amazon/txt/url.txt")
#URL_TO_SEARCH = [url.strip() for url in f.readlines()]
#f.close()

#
# Máxima cantidad de productos a obtener ( Aproximado * 2 requests )
MAX_CANT_TO_SEARCH = 10000 # == 40 prod aprox con status 200
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 0 # 250 ms of delay
CONCURRENT_REQUESTS = 10
CONCURRENT_REQUESTS_PER_DOMAIN = 10
#Maximum number of concurrent items (per response) to process in parallel in the Item Processor (default: 100)
CONCURRENT_ITEMS = 50
AUTOTHROTTLE_ENABLED = False
AUTOTHROTTLE_MAX_DELAY = 10
AUTOTHROTTLE_START_DELAY = 0.25
AUTOTHROTTLE_TARGET_CONCURRENCY  = 2.0
AUTOTHROTTLE_DEBUG = True
DOWNLOAD_TIMEOUT = 400
# Disable cookies (enabled by default)
COOKIES_ENABLED = True
COOKIES_DEBUG = False
TIMEZONE = 'America/Los_Angeles'

DOWNLOADER_MIDDLEWARES = {
    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':400,# Segundo
    #'amazon.middlewares.CustomProxyMiddleware':330, # Primero
    'scrapy_crawlera.CrawleraMiddleware': 50,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    # 'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 350,
    'amazon.middlewares.AmazonDownloaderMiddleware': 150,
}

# Proxy mode
# 0 = Every requests have different proxy
# 1 = Take only one proxy from the list and assign it to every requests
# 2 = Put a custom proxy to use in the settings
#PROXY_MODE = 0

ITEM_PIPELINES = {
    'amazon.pipelines.AmazonPipeline': 300,
}
# Crawlera Service
CRAWLERA_ENABLED = False
CRAWLERA_APIKEY = '86b52c0bde5d4de3a8c1d18964aa1a35'


