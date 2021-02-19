# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class MypttitemprojectPipeline:
    def process_item(self, item, spider):
        item['push'] = int(item['push'])
        return item


class DeleteNullTitlePipeline:
    def process_item(self, item, spider):
        title = item['title']
        if title:
            return item
        else:
            raise DropItem('found null item %s', item)


class DuplicatesTitlePipeline:
    def __init__(self):
        self.article = set()
        self.count = 0

    def process_item(self, item, spider):
        print('DuplicatesTitlePipeline count=', self.count)
        title = item['title']
        if title in self.article:
            raise DropItem('found null item %s', item)
        self.article.add(title)
        return(item)
