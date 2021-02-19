import scrapy
from bs4 import BeautifulSoup


class NewsSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        token = response.css(
            "input[name='csrf_token']::attr('value')").extract_first()
        # print(token)
        data = {
            'csrf_token': token,
            'username': 'user',
            'password': '123'
        }
        yield scrapy.FormRequest(url=self.start_urls[0], formdata=data, callback=self.parse_quotes)

    def parse_quotes(self, response):
        soup = BeautifulSoup(response.text)
        quotes = soup.select('div.quote')
        for q in quotes:
            print(q.select('a'))
