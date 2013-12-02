from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from blogscraper.items import BlogscraperItem
import csv

class MySpider(CrawlSpider):
    name = 'blogscraper'
    start_urls = ['http://wordpress.com/tags/']

    rules = (
        Rule(SgmlLinkExtractor(allow=('wordpress.com/tag/', )), callback='find_links', follow=True),
        )

    def __init__(self):
        super(MySpider, self).__init__()
        f = open('links_from_wp.csv', 'wb')
        f.close()

    def find_links(self, response):
        sel = Selector(response)
        links = sel.xpath("//a[@class='time-since']")
        # items = []
        urls_dict = {}

        for link in links: # why slicing?
            item = BlogscraperItem()
            item["url"] = link.xpath("@href").extract()[0]
        #     # items.append(item)
            urls_dict[item["url"]] = urls_dict.get(item["url"], 0) + 1
        # #adds urls scraped regularly from WP's "tags" page to list
        with open ('links_from_wp.csv', 'a') as csvfile: 
            writer=csv.writer(csvfile, delimiter="\n")
            writer.writerow(urls_dict.keys())

    

