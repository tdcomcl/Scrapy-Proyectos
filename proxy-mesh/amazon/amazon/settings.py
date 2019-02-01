# -*- coding: utf-8 -*-
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware

BOT_NAME = 'amazon'

SPIDER_MODULES = ['amazon.spiders']
NEWSPIDER_MODULE = 'amazon.spiders'

# Configuración
# Dominio a scrapp. 
DOMAIN_TO_SCRAPP = "https://www.amazon.com/"

# url con la búsqueda ( lego, impresoras, etc )
URL_TO_SEARCH = "https://www.amazon.com/s/s/ref=sr_nr_p_85_0?fst=as%3Aoff&rh=n%3A2335752011%2Ck%3Aradio%2Cp_85%3A2470955011&keywords=radio&ie=UTF8&qid=1548696045&rnid=2470954011"

# Máxima cantidad de productos a obtener ( Aproximado * 2 requests ) 
MAX_CANT_TO_SEARCH = 8000 # == 40 prod aprox con status 200
ROBOTSTXT_OBEY = True
# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 10
CONCURRENT_REQUESTS_PER_DOMAIN = 8
DOWNLOAD_DELAY = 0.35 # 250 ms of delay
AUTOTHROTTLE_ENABLED = False
DOWNLOAD_TIMEOUT = 640
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':400,# Segundo
    'amazon.middlewares.CustomProxyMiddleware':300, # Primero
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 350,
    #'amazon.middlewares.AmazonDownloaderMiddleware': 543,
}
ITEM_PIPELINES = {
    'amazon.pipelines.AmazonPipeline': 600,
}
AUTOTHROTTLE_DEBUG = True
