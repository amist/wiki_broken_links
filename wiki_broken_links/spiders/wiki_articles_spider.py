import scrapy
from wiki_broken_links.items import WikiArticleItem

class WikiArticlesSpider(scrapy.Spider):
    language = "he"
    base_domain = language + ".wikipedia.org"
    base_url = "http://" + base_domain
    
    name = "wiki_articles"
    allowed_domains = [base_domain]
    start_urls = [base_url + "/wiki/Special:AllPages"]
#    start_urls = ['http://en.wikipedia.org/w/index.php?title=Special%3AAllPages&from=User+testing&to=&namespace=0']  # right after 'User talk' chunk
    
    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)
        
        for a in response.xpath("//ul[@class='mw-allpages-chunk']/li[not(@class='allpagesredirect')]"):
            link = a.xpath('a/@href').extract()
            title = a.xpath('a/@title').extract()
#             print a
#             print link
#             print title
            item = WikiArticleItem()
#            item['title'] = title[0].encode('utf-8')
            item['title'] = title[0]
            yield item
            
            
        self.log('searching next page')
#        for a in response.xpath("//a[contains(text(), 'Next page')]"):
        for a in response.xpath("//div[@class='mw-allpages-nav']/a"):
#         for a in response.xpath("//a[@title='Special:AllPages']"):
#         for a in response.xpath("//div[@class='mw-allpages-nav']/a"):
#             self.log(response.xpath("//div[@class='mw-allpages-nav']/a"))
#             print a
            link = a.xpath("@href").extract()
#             print link
            request = scrapy.Request(self.base_url + link[0], callback=self.parse)
            yield request
            
