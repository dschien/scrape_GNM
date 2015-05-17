# -*- coding: utf-8 -*-

# Scrapy settings for scrape_GNM project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
# http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'GNM'

SPIDER_MODULES = ['scrape_GNM.spiders']
NEWSPIDER_MODULE = 'scrape_GNM.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrape_GNM (+http://www.yourdomain.com)'

DEPTH_LIMIT = 1

FEED_FORMAT = "jsonlines"
FEED_URI = "file:////Users/schien/workspaces/python/scrape_GNM/sitegraph.json"