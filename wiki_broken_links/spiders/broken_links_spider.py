import scrapy
import json
import httplib2
from wiki_broken_links.items import BrokenLinkItem

with open('articles.json') as articles_file:
    articles = json.load(articles_file)

class WikiArticlesSpider(scrapy.Spider):
    language = "he"
    base_domain = language + ".wikipedia.org"
    base_url = "http://" + base_domain
    
    name = "broken_links"
    allowed_domains = [base_domain]
    start_urls = ["https://he.wikipedia.org/wiki/" + x['title'] for x in articles]
    
    def __init__(self):
        self.http = httplib2.Http()
    
    def is_skip_url(self, urls):
#        print('---')
#        print(urls)
        if len(urls) == 0:
            return True
        url = urls[0]
        if len(url) == 0:
            return True
        if url[0] == '/':
            return True
        if url[0] == '#':
            return True
        if 'wikipedia.org' in url:
            return True
        if 'creativecommons.org' in url:
            return True
        if 'wikimediafoundation.org' in url:
            return True
        if 'mediawiki.org' in url:
            return True
        return False
    
    def get_link_status(self, url):
        try:
            response, content = self.http.request(url)
        except httplib2.CertificateHostnameMismatch:
            return "CertificateHostnameMismatch"
        except Exception as e:
            return str(e)
        return response.status
                                                             
    
    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)
        
        for a in response.xpath("//a"):
            if self.is_skip_url(a.xpath('@href').extract()):
                continue
            link = a.xpath('@href').extract()
            status = self.get_link_status(link[0])
            if status == 200:
                continue
            item = BrokenLinkItem()
            item['link'] = link
            item['article_url'] = response.url
            item['status'] = status
            yield item
