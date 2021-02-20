# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImagesrenameItem(scrapy.Item):
    imgurl = scrapy.Field()
    imgname = scrapy.Field()
