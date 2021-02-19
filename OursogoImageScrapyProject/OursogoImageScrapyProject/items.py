# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OursogoimagescrapyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class TopicPageItem(scrapy.Item):
    # define the fields for your item here like:
    # # name = scrapy.Field()
    # contentFilepaths = scrapy.Field()
    # contentPageUrls = scrapy.Field()
    image_filepath = scrapy.Field()
    contentpage_url = scrapy.Field()
