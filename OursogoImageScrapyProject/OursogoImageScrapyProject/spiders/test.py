import scrapy
from ..items import TopicPageItem


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['oursogo.com']
    start_urls = ['https://oursogo.com/forum-3-1.html']
    # default_headers = {
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #     'Accept-Encoding': 'gzip, deflate, sdch, br',
    #     'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    #     'Cache-Control': 'max-age=0',
    #     'Connection': 'keep-alive',
    #     'Host': 'www.douban.com',
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    # }

    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def make_requests_from_url(self, url):
        return scrapy.Request(url, dont_filter=True, cookies={'werA_viewadult': 'acceptrule'})

    def parse(self, response):
        list_contentUrls = response.css("th.new>a.xst")
        # print('-------->', list_contentUrls[0].css('::attr(href)').extract())
        # print('-------->', list_contentUrls[0].css('::text').extract())

        if list_contentUrls:
            for contentUrl in list_contentUrls:
                item = TopicPageItem()
                item['image_filepath'] = contentUrl.css('::text').extract()
                item['contentpage_url'] = contentUrl.css(
                    '::attr(href)').extract()
                yield item
