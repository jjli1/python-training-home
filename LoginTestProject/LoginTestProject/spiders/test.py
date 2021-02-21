import scrapy


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
        if "authentication failed" in response.text:
            self.log("Login failed", level=log.ERROR)
            return
