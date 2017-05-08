# -*- coding: utf-8 -*-
import os
import scrapy
from scrapy.conf import settings


class ReutersSpiderSpider(scrapy.Spider):
    name = "reuters_spider"
    allowed_domains = ["reuters.com"]

    def start_requests(self):

        with open(os.path.join(settings.get("BASE_DIR"), 'symbols.txt')) as f:
            for line in f:
                yield scrapy.Request("http://www.reuters.com/finance/stocks/analyst?symbol=" + line.strip(), callback=self.parse_page)

    def parse_page(self, response):
        body = response.body
        folder_path = os.path.join(settings.get("BASE_DIR"), "webpages")
        filename = response.url.split("=")[-1]
        with open(os.path.join(folder_path, filename + ".html"), "wb") as f:
            f.write(body)

        yield {"response_status": response.status, "symbol": filename, "url":response.url}
