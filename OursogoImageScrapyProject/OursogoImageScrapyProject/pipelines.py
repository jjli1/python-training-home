# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.exceptions import DropItem
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class OursogoimagescrapyprojectPipeline:
    def process_item(self, item, spider):
        return item


class OursogoImgDownloadPipeline(ImagesPipeline):
    default_headers = {
        'accept': 'image/webp,image/*,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'cookie': 'bid=yQdC/AzTaCw',
        'referer': 'https://www.douban.com/photos/photo/2370443040/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }

    def get_media_requests(self, item, info):
        image_url = item['image_url']
        self.default_headers['referer'] = image_url
        print('############get_media_requests:', image_url)
        yield Request(image_url, headers=self.default_headers)

    def item_completed(self, results, item, info):
        print('========>results', results)
        image_paths = [x['path'] for ok, x in results if ok]
        print('========>image_paths', image_paths)
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item


class TextPipeline(object):
    def process_item(self, item, spider):
        print('------------>process_item')
        return item
