# -*- coding: utf-8 -*-
"""
reuters spider pipeline,
will cache all items in a json file then before the spider terminates, it will read all items again from the file
and insert them to sqlite database
"""
import json
import os


class ReutersPipeline(object):
    """
    reuters spider item pipeline, used to store scrapped items to sqlite db
    """
    cache_file = None
    cache_file_name = 'cash_symbols.json'

    def open_spider(self, spider):
        """
        create the cache json file
        :param spider: 
        :return: 
        """
        self.cache_file = open(self.cache_file_name, 'wb')
        self.cache_file.write("[")

    def close_spider(self, spider):
        """
        will get called when the spider is closing.
        will read data from the cache file, insert them to the database, delete the cache file.
        :param spider: 
        :return: 
        """
        self.cache_file.seek(-2, os.SEEK_END)
        self.cache_file.truncate()
        self.cache_file.write("]")
        self.cache_file.close()

        # open the file again and insert all items to the database

    def process_item(self, item, spider):
        """
        cache the scrapped item to the cache json file
        :param item: 
        :param spider: 
        :return: 
        """
        line = json.dumps(dict(item)) + ",\n"
        self.cache_file.write(line)
        return item






