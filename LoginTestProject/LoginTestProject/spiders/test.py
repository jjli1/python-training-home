import scrapy
import logging


class TestSpider(scrapy.Spider):
    name = 'test'
    start_urls = [
        'https://oursogo.com//member.php?mod=logging&action=login&loginsubmit=yes&loginhash=L5DHz']

    def parse(self, response):
        return [scrapy.FormRequest.from_response(response,
                                                 formdata={
                                                     'username': self.username, 'password': self.password},
                                                 callback=self.after_login)]

    def after_login(self, response):
        # check login succeed before going on
        if "抱歉，您所在的用戶組(訪客)無法進行此操作" in response.text:
            # self.log("Login failed", level=log.ERROR)
            print("---->Login fail")
        else:
            print("---->Login success")
        return
