import scrapy


# class ExampleSpider(scrapy.Spider):
#     name = 'ppt_movie'

#     def start_requests(self):
#         yield scrapy.Request('https://www.ptt.cc/bbs/movie/index.html',headers={'User-Agent': 'Mozilla/5.0'},callback=self.)

#     def parse(self, response):
#         pass

# class ExampleSpider(scrapy.Spider):
#     name = 'ptt'
#     allowed_domains = ['ptt.com']
#     start_urls = [
#         'https://www.ptt.cc/bbs/Food/index.html',
#         'https://www.ptt.cc/bbs/movie/index.html',
#     ]

#     def parse(self, response):
#         self.logger.info('A response from %s just arrived!', response.url)

class ExampleSpider(scrapy.Spider):
    name = 'ptt'
    allowed_domains = ['ptt.com']

    def start_requests(self):
        yield scrapy.Request('https://www.ptt.cc/bbs/Food/index.html', callback=self.parse)
        yield scrapy.Request('https://www.ptt.cc/bbs/movie/index.html', self.parse)

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        self.logger.info(response.text)
