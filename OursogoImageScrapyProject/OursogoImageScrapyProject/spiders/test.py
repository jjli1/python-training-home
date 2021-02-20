import scrapy
from ..items import ImageItem


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['oursogo.com']
    start_urls = ['https://oursogo.com/forum-18-1.html']
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

        if list_contentUrls:
            for contentUrl in list_contentUrls:
                image_filepath = contentUrl.css('::text')[0].extract()
                contentpage_url = contentUrl.css('::attr(href)')[0].extract()
                # print(image_filepath, contentpage_url)
                yield(scrapy.Request(contentpage_url, callback=self.contentPageParse, dont_filter=True))
                break

    def contentPageParse(self, response):
        imageUrlList = response.css('ignore_js_op img::attr(file)').extract()
        for imageUrl in imageUrlList:
            # print('-->', 'https://'+self.allowed_domains[0]+'/'+imageUrl)
            item = ImageItem()
            item['image_path'] = 'f:/temp'
            item['image_url'] = 'https://' + \
                self.allowed_domains[0]+'/'+imageUrl
            yield item

    # def contentPageParse(self, response):
    #     imageUrlList = response.css('ignore_js_op img::attr(file)').extract()
    #     print('------------------->imageUrlList=', imageUrlList)
    #     if imageUrlList:
    #         item = ImagesItem()
    #         item['image_urls'] = imageUrlList
    #         yield item
