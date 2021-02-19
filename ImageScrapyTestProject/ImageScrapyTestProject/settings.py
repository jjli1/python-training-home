# Scrapy settings for ImageScrapyTestProject project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ImageScrapyTestProject'

SPIDER_MODULES = ['ImageScrapyTestProject.spiders']
NEWSPIDER_MODULE = 'ImageScrapyTestProject.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'ImageScrapyTestProject.middlewares.ImagescrapytestprojectSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #    'ImageScrapyTestProject.middlewares.ImagescrapytestprojectDownloaderMiddleware': 543,
    'ImageScrapyTestProject.middlewares.RandomProxyMiddleware': 745,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'ImageScrapyTestProject.pipelines.ImagescrapytestprojectPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

ITEM_PIPELINES = {
    'ImageScrapyTestProject.pipelines.DoubanImgDownloadPipeline': 300,
}
IMAGES_STORE = 'z:\\TEMP'
IMAGES_EXPIRES = 90
PROXY_LIST_FILE = 'f:/proxy.json'
PROXYLIST1 = ['http://116.203.23.252:3128', 'http://203.150.113.9:8080', 'http://115.127.162.170:8080', 'http://167.249.181.236:8080', 'http://191.97.19.93:999', 'http://4.14.219.157:3128', 'http://150.129.148.88:35101', 'http://150.129.56.138:31111', 'http://185.198.188.51:8080', 'http://95.38.171.201:8080',
              'http://190.57.143.66:50719', 'http://188.166.215.141:3128', 'http://36.83.26.219:8080', 'http://171.103.158.70:8080', 'http://78.140.201.254:11335', 'http://178.47.141.85:2580', 'http://203.176.135.102:52234', 'http://213.6.136.150:8080', 'http://81.91.219.23:3128', 'http://193.178.50.49:3128']
PROXYLIST2 = ['http://4.14.219.157:3128', 'http://209.203.130.59:23500', 'http://50.201.51.216:8080', 'http://100.24.216.83:80', 'http://84.17.35.129:3128',
              'http://104.248.123.76:18080', 'http://47.90.132.228:3128', 'http://104.248.61.108:3128', 'http://35.231.234.221:3128', 'http://35.196.22.228:3128']
