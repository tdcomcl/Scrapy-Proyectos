# -*- coding: utf-8 -*-
# Scrapy settings for amazon project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware

BOT_NAME = 'amazon'

SPIDER_MODULES = ['amazon.spiders']
NEWSPIDER_MODULE = 'amazon.spiders'

SPIDER_SETTINGS = {
    'spider1': 'amazon.spiders.amazon',
    'spider2': 'amazon.spiders.amazon_with_asin',
}

# Configuración
# Dominio a scrapp. 
DOMAIN_TO_SCRAPP = "https://www.amazon.es/"

# url con la búsqueda ( lego, impresoras, etc )
LEGO_URL = "https://www.amazon.es/s/gp/search/ref=sr_nr_p_6_0?fst=as%3Aoff%2Cp90x%3A1&rh=n%3A165793011%2Cn%3A166092011%2Ck%3Alego%2Cp_85%3A2470955011%2Cp_6%3AATVPDKIKX0DER&keywords=lego&ie=UTF8&qid=1547312518&rnid=275224011"
CAR_URL = "https://www.amazon.es/s/ref=nb_sb_noss?url=node%3D166092011&field-keywords=car&rh=n%3A165793011%2Cn%3A166092011%2Ck%3Acar"
PRINTER_URL = "https://www.amazon.es/s/ref=nb_sb_noss?url=search-alias%3Delectronics-intl-ship&field-keywords=printer&rh=i%3Aelectronics-intl-ship%2Ck%3Aprinter"
FUNKO_POP = "https://www.amazon.es/s/ref=nb_sb_ss_c_1_5?url=search-alias%3Daps&field-keywords=funko+pop&sprefix=funko%2Caps%2C303&crid=6XMZ4WU1XZSF"

URL_TO_SEARCH = FUNKO_POP

# Máxima cantidad de productos a obtener ( Aproximado * 2 requests ) 
MAX_CANT_TO_SEARCH = 50000 # == 40 prod aprox con status 200


#URL_TO_SEARCH_WITH_ASIN = []

with open('/home/ubuntu/arana-amazon/amazon-with_asin/mimo.txt') as f:
    URL_TO_SEARCH_WITH_ASIN = [url.strip() for url in f.readlines()]

# Http Proxy
#HTTP_PROXY = 'http://dcortesnet:Iamsupport123@us-wa.proxymesh.com:31280'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'amazon (+http://www.yourdomain.com)'
#USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
# Obey robots.txt rules
ROBOTSTXT_OBEY = True
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 10
# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16
# Disable cookies (enabled by default)
#COOKIES_ENABLED = False
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False
# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'amazon.middlewares.AmazonSpiderMiddleware': 543,
#}
# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':200,# Segundo
    'amazon.middlewares.CustomProxyMiddleware':330, # Primero
    'scrapy_crawlera.CrawleraMiddleware': 300,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 350,
	'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90
    #'amazon.middlewares.AmazonDownloaderMiddleware': 543,
}
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}
# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'amazon.pipelines.AmazonPipeline': 600,
}
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False
# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# Crawlera Service
CRAWLERA_ENABLED = True
CRAWLERA_APIKEY = '86b52c0bde5d4de3a8c1d18964aa1a35'

"""
Para lograr tasas de rastreo más altas al usar Crawlera con Scrapy, se recomienda deshabilitar el complemento Auto Throttle y aumentar el número máximo de solicitudes simultáneas. También es posible que desee aumentar la descarga
También es posible que desee aumentar el tiempo de espera de descarga. Aquí hay una lista de configuraciones que logran ese propósito:
"""
CONCURRENT_ITEMS = 1
CONCURRENT_REQUESTS = 50
CONCURRENT_REQUESTS_PER_DOMAIN = 8
AUTOTHROTTLE_ENABLED = True
DOWNLOAD_TIMEOUT = 600
CRAWLERA_PRESERVE_DELAY = True
DOWNLOAD_DELAY = 0.6 # 250 ms of delay
AUTOTHROTTLE_ENABLED = False
AUTOTHROTTLE_TARGET_CONCURRENCY  = 2.0
COOKIES_ENABLED = False
COOKIES_DEBUG = False
RETRY_TIMES = 5
DOWNLOAD_MAXSIZE = 0 
DOWNLOAD_WARNSIZE = 0

TIMEZONE = 'America/Los_Angeles'


"""
Los 429 que está recibiendo son porque está enviando más solicitudes de las que permite su plan. El plan del plan C10 permite hasta 10 solicitudes simultáneas en total, por lo que reducir sus solicitudes simultáneas enviadas a Crawlera a <= 10 resolverá el problema.
"""

