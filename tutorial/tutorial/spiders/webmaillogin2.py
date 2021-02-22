import scrapy
import re


class Webmaillogin2Spider(scrapy.Spider):
    name = 'webmaillogin2'
    allowed_domains = ['webmail.cht.com.tw']
    start_urls = [
        'https://webmail.cht.com.tw/cgi-bin/msg_list?cmd=show_list&templ=ajax&mbox=@']
    login_url = 'https://webmail.cht.com.tw/cgi-bin/login'

    def start_requests(self):  # 請求時攜帶Cookies
        print('------>1')
        form_data = {
            'remember': '',
            'USERID': '',
            'PASSWD': ''
        }
        yield scrapy.FormRequest(self.login_url, formdata=form_data, callback=self.after_login)

    def parse(self, response):
        print('------>parse',
              re.sub(r'[？\\*|“<>:/]', '', response.text.encode('raw_unicode_escape').decode('unicode_escape')))

    def after_login(self, response):  # 驗證是否請求成功
        # print('------>', re.findall('Discover interesting projects and people to populate your personal',response.body.decode()))
        # https://webmail.cht.com.tw/cgi-bin/start?m=1046575912&wrap=1
        # document.location.replace("/cgi-bin/start?m=707112807&wrap=1");
        # https://webmail.cht.com.tw/cgi-bin/start?m=707112807&wrap=1
        # Request URL: https://webmail.cht.com.tw/cgi-bin/msg_list?cmd=show_list&templ=ajax&mbox=@&m=61274829&m=89858840

        print('------>2', response.body.decode())
        redirect_url = response.urljoin(re.search(
            'document\.location\.replace\("(.+)"', response.body.decode()).group(1))
        print('------>3', redirect_url)
        yield scrapy.Request('https://webmail.cht.com.tw/cgi-bin/msg_list?cmd=show_list&templ=ajax&mbox=@', callback=self.parse)
