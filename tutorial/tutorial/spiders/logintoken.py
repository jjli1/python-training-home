import scrapy
from scrapy.http import FormRequest


class LogintokenSpider(scrapy.Spider):
    name = 'logintoken'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        # csrf_token = response.xpath('//*[@name='csrf_token']/@value').extract_first()')
        csrf_token = response.css(
            "form input[name='csrf_token']::attr(value)").extract_first()
        print('----->csrf_token=', csrf_token)
        yield scrapy.FormRequest.from_response(response,
                                               formdata={
                                                   'csrf_token': csrf_token, 'username': 'user', 'password': 'pass'},
                                               callback=self.parse_after_login)

    def parse_after_login(self, response):
        print('----->parse_after_login')
        print('-------->response.url=',
              response.css("a[href='/logout']::text").extract_first())
