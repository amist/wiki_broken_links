import scrapy


class WikiArticleItem(scrapy.Item):
    title = scrapy.Field()


class BrokenLinkItem(scrapy.Item):
    article_url = scrapy.Field()
    link = scrapy.Field()
    status = scrapy.Field()
    
