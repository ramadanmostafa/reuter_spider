# -*- coding: utf-8 -*-
"""
item class to store scrapped information from reuters financial page
"""
import scrapy


class ReutersItem(scrapy.Item):
    """
    column names for scrapped information
    """
    response_status = scrapy.Field()
    response_url = scrapy.Field()
    symbol = scrapy.Field()
    date_scrapped = scrapy.Field()
    company_name = scrapy.Field()
    wrong_symbol = scrapy.Field()
    No_consensus_analysis_data_available = scrapy.Field()

    sales_consensus_box1 = scrapy.Field()
    sales_consensus_box2 = scrapy.Field()
    sales_consensus_box3 = scrapy.Field()
    sales_consensus_box4 = scrapy.Field()
    earning_consensus_box1 = scrapy.Field()
    earning_consensus_box2 = scrapy.Field()
    earning_consensus_box3 = scrapy.Field()
    earning_consensus_box4 = scrapy.Field()
    earning_consensus_box5 = scrapy.Field()

    sales_estimates_box1 = scrapy.Field()
    sales_estimates_box2 = scrapy.Field()
    sales_estimates_box3 = scrapy.Field()
    sales_estimates_box4 = scrapy.Field()
    earning_estimates_box1 = scrapy.Field()
    earning_estimates_box2 = scrapy.Field()
    earning_estimates_box3 = scrapy.Field()
    earning_estimates_box4 = scrapy.Field()
    earning_estimates_box5 = scrapy.Field()

    sales_mean_box1 = scrapy.Field()
    sales_mean_box2 = scrapy.Field()
    sales_mean_box3 = scrapy.Field()
    sales_mean_box4 = scrapy.Field()
    earning_mean_box1 = scrapy.Field()
    earning_mean_box2 = scrapy.Field()
    earning_mean_box3 = scrapy.Field()
    earning_mean_box4 = scrapy.Field()
    earning_mean_box5 = scrapy.Field()

    sales_high_box1 = scrapy.Field()
    sales_high_box2 = scrapy.Field()
    sales_high_box3 = scrapy.Field()
    sales_high_box4 = scrapy.Field()
    earning_high_box1 = scrapy.Field()
    earning_high_box2 = scrapy.Field()
    earning_high_box3 = scrapy.Field()
    earning_high_box4 = scrapy.Field()
    earning_high_box5 = scrapy.Field()

    sales_low_box1 = scrapy.Field()
    sales_low_box2 = scrapy.Field()
    sales_low_box3 = scrapy.Field()
    sales_low_box4 = scrapy.Field()
    earning_low_box1 = scrapy.Field()
    earning_low_box2 = scrapy.Field()
    earning_low_box3 = scrapy.Field()
    earning_low_box4 = scrapy.Field()
    earning_low_box5 = scrapy.Field()

    sales_year_ago_box1 = scrapy.Field()
    sales_year_ago_box2 = scrapy.Field()
    sales_year_ago_box3 = scrapy.Field()
    sales_year_ago_box4 = scrapy.Field()
    earning_year_ago_box1 = scrapy.Field()
    earning_year_ago_box2 = scrapy.Field()
    earning_year_ago_box3 = scrapy.Field()
    earning_year_ago_box4 = scrapy.Field()
    earning_year_ago_box5 = scrapy.Field()
