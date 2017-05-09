# -*- coding: utf-8 -*-


class ReutersPipeline(object):

    def process_item(self, item, spider):
        """
        get called after ReutersSpiderSpider.parse_page method to store the parsed data to the database
        :param item: 
        :param spider: 
        :return: 
        """
        return item
