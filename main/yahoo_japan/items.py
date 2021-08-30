# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YahooJapanItem(scrapy.Item):
    headline = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()


class YahooJapanNewsItem(scrapy.Item):
    headline = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
