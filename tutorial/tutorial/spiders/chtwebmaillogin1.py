import scrapy
import re


class GithubLogin2Spider(scrapy.Spider):
    name = 'webmaillogin1'
    allowed_domains = ['webmail.cht.com.tw']
    start_urls = ['https://webmail.cht.com.tw/cgi-bin/login']
    # https://webmail.cht.com.tw/cgi-bin/msg_list?cmd=show_list&templ=ajax&mbox=@

    def parse(self, response):  # 發送Post請求獲取Cookies
        print('------>1')
        form_data = {
            'remember': '',
            'USERID': 'jjli',
            'PASSWD': 'feb@1020'
        }
        yield scrapy.FormRequest.from_response(response, formdata=form_data, callback=self.after_login, dont_filter=True)

    def after_login(self, response):  # 驗證是否請求成功
        # print('------>', re.findall('Discover interesting projects and people to populate your personal',
        #                             response.body.decode()))
        print('------>2', response.url)
