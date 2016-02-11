import scrapy


class WikiArticleItem(scrapy.Item):
    title = scrapy.Field()


class ArticleStatItem(scrapy.Item):
    title = scrapy.Field()
    stats = scrapy.Field()
    
