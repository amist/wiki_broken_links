import scrapy.cmdline

def main():
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'wiki_articles', '-o', 'articles.json'])
#     scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'page_statistics', '-o', 'stats.json'])

if  __name__ =='__main__':
    main()