import urlparse
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.selector import HtmlXPathSelector

from scrape_GNM.items import GNMPageItem

__author__ = 'schien'


class GNMSpider(CrawlSpider):
    name = "gnm"
    allowed_domains = ["theguardian.com", "guardian.co.uk"]
    start_urls = ["http://www.theguardian.com/uk", ]
    rules = [Rule(LxmlLinkExtractor(deny_domains=('profile.theguardian.com', 'discussion.theguardian.com',)),
                  callback='parse_page', follow=True)]

    def parse_page(self, response):
        hxs = HtmlXPathSelector(response)

        page = GNMPageItem()
        page['url'] = response.url
        page['title'] = response.xpath("/html/head/title/text()").extract()

        llinks = []
        for anchor in hxs.select('//a[@href]'):
            href = anchor.select('@href').extract()[0]
            if not href.lower().startswith("javascript"):
                llinks.append(urlparse.urljoin(response.url, href))
        page['linkedurls'] = llinks

        return page