import scrapy
import random


class ProxyExampleSpider(scrapy.Spider):
    name = "test"
    # start_urls = ['https://httpbin.org/ip']

    def start_requests(self):
        for i in range(10):
            yield scrapy.Request(random.choice(['http', 'https'])+'://httpbin.org/ip', dont_filter=True)

    def parse(self, response):
        # print('----->response.text<-', response.meta)
        print(response.text)
