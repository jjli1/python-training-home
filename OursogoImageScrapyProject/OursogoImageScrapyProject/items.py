# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OursogoimagescrapyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ImagesrenameItem(scrapy.Item):
    domainurl = scrapy.Field()
    imgurl = scrapy.Field()
    imgname = scrapy.Field()
