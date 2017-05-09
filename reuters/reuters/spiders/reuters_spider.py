# -*- coding: utf-8 -*-
import os
from datetime import datetime
import scrapy
from scrapy.conf import settings
from ..items import ReutersItem


class ReutersSpiderSpider(scrapy.Spider):
    """
    scrapy spider to crawl reuters.com
    it takes a txt file contains symbols (one for each line) and get information about this symbol.
    """
    name = "reuters_spider"
    allowed_domains = ["reuters.com"]
    BASE_URL = "http://www.reuters.com/finance/stocks/analyst?symbol=%s"

    def start_requests(self):
        """
        generate a scrapy request for each symbol from the input file
        :return: 
        """
        with open(
                os.path.join(
                    settings.get("BASE_DIR"),
                    'symbols_test.txt'
                )
        ) as file_handle:
            for line in file_handle:
                yield scrapy.Request(
                    self.BASE_URL % line.strip(),
                    callback=self.parse_page
                )

    # div
    #
    # class ="column1 gridPanel grid8"
    def parse_page(self, response):
        """
        get called once for each request generated from start_requests method
        :param response: 
        :return: 
        """
        body = response.body
        folder_path = os.path.join(settings.get("BASE_DIR"), "webpages")
        filename = response.url.split("=")[-1]
        with open(os.path.join(folder_path, filename + ".html"), "wb") as f:
            f.write(body)

        item = ReutersItem()
        item["response_status"] = response.status
        item["response_url"] = response.url
        item["symbol"] = filename
        item["date"] = str(datetime.now().date())
        yield item
