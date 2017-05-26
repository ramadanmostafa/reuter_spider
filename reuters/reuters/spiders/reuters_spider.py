# -*- coding: utf-8 -*-
"""
scrapy spider to get financial information from reuters.com based on a specific symbol
"""
import os
import scrapy
from scrapy.conf import settings
from .item_parser import financial_parser
import logging



class ReutersSpiderSpider(scrapy.Spider):
    """
    scrapy spider to crawl reuters.com
    it takes a txt file contains symbols (one for each line) and get information about this symbol.
    """
    name = "reuters_spider"
    allowed_domains = ["reuters.com"]
    BASE_URL = "http://www.reuters.com/finance/stocks/financialHighlights?symbol={}"

    def start_requests(self):
        """
        generate a scrapy request for each symbol from the input file
        :return:
        """
        symbols_file_path = os.path.join(settings.get("BASE_DIR"), 'symbols.txt')
        with open(symbols_file_path, 'r') as file_handle:
            for line in file_handle:
                print(self.BASE_URL.format(line.strip()))
                yield scrapy.Request(
                    self.BASE_URL.format(line.strip()),
                    callback=self.parse_page
                )

    def parse_page(self, response):
        """
        get called once for each request generated from start_requests method
        :param response:
        :return:
        """
        # body = response.body
        # folder_path = os.path.join(settings.get("BASE_DIR"), "webpages")
        # filename = response.url.split("=")[-1]
        # with open(os.path.join(folder_path, filename + ".html"), "wb") as f:
        #     f.write(body)
        yield financial_parser(response)
