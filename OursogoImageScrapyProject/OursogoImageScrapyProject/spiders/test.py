import scrapy
from ..items import ImagesrenameItem


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

    def contentPageParse(self, response):
        item = ImagesrenameItem()
        item['domainurl'] = 'https://oursogo.com/'
        # 注意imgurls是一个集合也就是多张图片
        item['imgurl'] = response.css('ignore_js_op img::attr(file)').extract()
        # 抓取文章标题作为图集名称
        item['imgname'] = response.css(
            "h1.ts > a#thread_subject ::text").extract_first()
        yield item
