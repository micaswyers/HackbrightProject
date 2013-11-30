from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from blog.items import BlogItem
from urllib2 import urlopen

class MySpider(CrawlSpider):
    name = 'blogscraper'
    start_urls = ['http://wordpress.com/tags/']

    rules = (
        Rule(SgmlLinkExtractor(allow=('wordpress.com/tag/', )), callback='find_links', follow=True),
        )

    def find_links(self, response):
        sel = Selector(response)
        links = sel.xpath("//a[@class='time-since']")
        items = []

        for link in links[:10]:
            item = BlogItem()
            item["url"] = link.xpath("@href").extract()
            items.append(item)
        return items



    # def parse_item(self, response):
    #     self.log('FOUND A BLOG PAGE: %s' % response.url)

    #     sel = Selector(response)
    #     item =  BlogItem()
    #     item["url"] = sel.xpath("a/@href").extract()
    #     return item