import scrapy
import re
from ..items import DoubanImgsItem


class ExampleSpider(scrapy.Spider):
    name = 'download_douban'
    start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    default_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'www.douban.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        'Cookie': '__cfduid=d3fd57ddf9db0c1a8980ef61da4e1eae61613465063; werA_0ff6_saltkey=44rDp4Yp; werA_0ff6_lastvisit=1613461433; __cf_bm=1d098953d53dc17fb76537c8c9e1cc98ebf2956a-1613465063-1800-AYEjGhCVAiUsuVrXfG9Hmd2A7x+XP19lcx2ApCWfNlV4y3oJnXh+6EyZKp1GOh/vhuIEc69CoFjtXJlwm6Hdc0w=; werA_0ff6_sendmail=1; _ga=GA1.2.61435557.1613465072; _gid=GA1.2.702241666.1613465072; _gat_gtag_UA_6272726_1=1; __gads=ID=aee781f5096dd984-221a0af40ac60065:T=1613465073:RT=1613465073:S=ALNI_MaFtt-sUxGIeP20uMM6W6TxCav5pw; werA_0ff6_sid=xSf3EA; werA_0ff6_lastact=1613465054	forum.php	forumdisplay;werA_viewadult=acceptrule'
    }

    def make_requests_from_url(self, url):
        return scrapy.http.Request(url, headers=self.default_headers)

    def parse(self, response):
        list_imgs = response.css(".post img::attr(src)").extract()
        print('------------------->list_imgs=', list_imgs)
        if list_imgs:
            item = DoubanImgsItem()
            item['image_urls'] = list_imgs
            yield item
