# -*- coding: utf-8 -*-
"""
item class to store scrapped information from reuters financial page
"""
import scrapy


class ReutersItem(scrapy.Item):
    """
    column names for scrapped information
    286 fields
    """
    # information about the page
    response_status = scrapy.Field()
    response_url = scrapy.Field()
    symbol = scrapy.Field()
    date_scrapped = scrapy.Field()
    company_name = scrapy.Field()
    wrong_symbol = scrapy.Field()
    No_consensus_analysis_data_available = scrapy.Field()

    # CONSENSUS ESTIMATES ANALYSIS
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

    # REVENUE & EARNINGS PER SHARE
    revenue_earnings_per_share_year_box1 = scrapy.Field()
    revenue_earnings_per_share_year_box2 = scrapy.Field()
    revenue_earnings_per_share_year_box3 = scrapy.Field()

    revenue_earnings_per_share_month_box1 = scrapy.Field()
    revenue_earnings_per_share_month_box2 = scrapy.Field()
    revenue_earnings_per_share_month_box3 = scrapy.Field()
    revenue_earnings_per_share_month_box4 = scrapy.Field()
    revenue_earnings_per_share_month_box5 = scrapy.Field()
    revenue_earnings_per_share_month_box6 = scrapy.Field()
    revenue_earnings_per_share_month_box7 = scrapy.Field()
    revenue_earnings_per_share_month_box8 = scrapy.Field()
    revenue_earnings_per_share_month_box9 = scrapy.Field()
    revenue_earnings_per_share_month_box10 = scrapy.Field()

    revenue_box1 = scrapy.Field()
    revenue_box2 = scrapy.Field()
    revenue_box3 = scrapy.Field()
    revenue_box4 = scrapy.Field()
    revenue_box5 = scrapy.Field()
    revenue_box6 = scrapy.Field()
    revenue_box7 = scrapy.Field()
    revenue_box8 = scrapy.Field()
    revenue_box9 = scrapy.Field()
    revenue_box10 = scrapy.Field()

    earnings_per_share_box1 = scrapy.Field()
    earnings_per_share_box2 = scrapy.Field()
    earnings_per_share_box3 = scrapy.Field()
    earnings_per_share_box4 = scrapy.Field()
    earnings_per_share_box5 = scrapy.Field()
    earnings_per_share_box6 = scrapy.Field()
    earnings_per_share_box7 = scrapy.Field()
    earnings_per_share_box8 = scrapy.Field()
    earnings_per_share_box9 = scrapy.Field()
    earnings_per_share_box10 = scrapy.Field()

    # VALUATION RATIOS
    valuation_ratios_name_box1 = scrapy.Field()
    valuation_ratios_company_box1 = scrapy.Field()
    valuation_ratios_industry_box1 = scrapy.Field()
    valuation_ratios_sector_box1 = scrapy.Field()

    valuation_ratios_name_box2 = scrapy.Field()
    valuation_ratios_company_box2 = scrapy.Field()
    valuation_ratios_industry_box2 = scrapy.Field()
    valuation_ratios_sector_box2 = scrapy.Field()

    valuation_ratios_name_box3 = scrapy.Field()
    valuation_ratios_company_box3 = scrapy.Field()
    valuation_ratios_industry_box3 = scrapy.Field()
    valuation_ratios_sector_box3 = scrapy.Field()

    valuation_ratios_name_box4 = scrapy.Field()
    valuation_ratios_company_box4 = scrapy.Field()
    valuation_ratios_industry_box4 = scrapy.Field()
    valuation_ratios_sector_box4 = scrapy.Field()

    valuation_ratios_name_box5 = scrapy.Field()
    valuation_ratios_company_box5 = scrapy.Field()
    valuation_ratios_industry_box5 = scrapy.Field()
    valuation_ratios_sector_box5 = scrapy.Field()

    valuation_ratios_name_box6 = scrapy.Field()
    valuation_ratios_company_box6 = scrapy.Field()
    valuation_ratios_industry_box6 = scrapy.Field()
    valuation_ratios_sector_box6 = scrapy.Field()

    valuation_ratios_name_box7 = scrapy.Field()
    valuation_ratios_company_box7 = scrapy.Field()
    valuation_ratios_industry_box7 = scrapy.Field()
    valuation_ratios_sector_box7 = scrapy.Field()

    valuation_ratios_name_box8 = scrapy.Field()
    valuation_ratios_company_box8 = scrapy.Field()
    valuation_ratios_industry_box8 = scrapy.Field()
    valuation_ratios_sector_box8 = scrapy.Field()

    valuation_ratios_name_box9 = scrapy.Field()
    valuation_ratios_company_box9 = scrapy.Field()
    valuation_ratios_industry_box9 = scrapy.Field()
    valuation_ratios_sector_box9 = scrapy.Field()

    # dividends
    dividends_name_box1 = scrapy.Field()
    dividends_company_box1 = scrapy.Field()
    dividends_industry_box1 = scrapy.Field()
    dividends_sector_box1 = scrapy.Field()

    dividends_name_box2 = scrapy.Field()
    dividends_company_box2 = scrapy.Field()
    dividends_industry_box2 = scrapy.Field()
    dividends_sector_box2 = scrapy.Field()

    dividends_name_box3 = scrapy.Field()
    dividends_company_box3 = scrapy.Field()
    dividends_industry_box3 = scrapy.Field()
    dividends_sector_box3 = scrapy.Field()

    dividends_name_box4 = scrapy.Field()
    dividends_company_box4 = scrapy.Field()
    dividends_industry_box4 = scrapy.Field()
    dividends_sector_box4 = scrapy.Field()

    # GROWTH RATES
    growth_rates_name_box1 = scrapy.Field()
    growth_rates_name_box2 = scrapy.Field()
    growth_rates_name_box3 = scrapy.Field()
    growth_rates_name_box4 = scrapy.Field()
    growth_rates_name_box5 = scrapy.Field()
    growth_rates_name_box6 = scrapy.Field()
    growth_rates_name_box7 = scrapy.Field()

    growth_rates_company_box1 = scrapy.Field()
    growth_rates_company_box2 = scrapy.Field()
    growth_rates_company_box3 = scrapy.Field()
    growth_rates_company_box4 = scrapy.Field()
    growth_rates_company_box5 = scrapy.Field()
    growth_rates_company_box6 = scrapy.Field()
    growth_rates_company_box7 = scrapy.Field()

    growth_rates_industry_box1 = scrapy.Field()
    growth_rates_industry_box2 = scrapy.Field()
    growth_rates_industry_box3 = scrapy.Field()
    growth_rates_industry_box4 = scrapy.Field()
    growth_rates_industry_box5 = scrapy.Field()
    growth_rates_industry_box6 = scrapy.Field()
    growth_rates_industry_box7 = scrapy.Field()

    growth_rates_sector_box1 = scrapy.Field()
    growth_rates_sector_box2 = scrapy.Field()
    growth_rates_sector_box3 = scrapy.Field()
    growth_rates_sector_box4 = scrapy.Field()
    growth_rates_sector_box5 = scrapy.Field()
    growth_rates_sector_box6 = scrapy.Field()
    growth_rates_sector_box7 = scrapy.Field()

    # FINANCIAL STRENGTH
    financial_strength_name_box1 = scrapy.Field()
    financial_strength_company_box1 = scrapy.Field()
    financial_strength_industry_box1 = scrapy.Field()
    financial_strength_sector_box1 = scrapy.Field()

    financial_strength_name_box2 = scrapy.Field()
    financial_strength_company_box2 = scrapy.Field()
    financial_strength_industry_box2 = scrapy.Field()
    financial_strength_sector_box2 = scrapy.Field()

    financial_strength_name_box3 = scrapy.Field()
    financial_strength_company_box3 = scrapy.Field()
    financial_strength_industry_box3 = scrapy.Field()
    financial_strength_sector_box3 = scrapy.Field()

    financial_strength_name_box4 = scrapy.Field()
    financial_strength_company_box4 = scrapy.Field()
    financial_strength_industry_box4 = scrapy.Field()
    financial_strength_sector_box4 = scrapy.Field()

    financial_strength_name_box5 = scrapy.Field()
    financial_strength_company_box5 = scrapy.Field()
    financial_strength_industry_box5 = scrapy.Field()
    financial_strength_sector_box5 = scrapy.Field()

    # PROFITABILITY RATIOS
    profitability_ratios_name_box1 = scrapy.Field()
    profitability_ratios_company_box1 = scrapy.Field()
    profitability_ratios_industry_box1 = scrapy.Field()
    profitability_ratios_sector_box1 = scrapy.Field()

    profitability_ratios_name_box2 = scrapy.Field()
    profitability_ratios_company_box2 = scrapy.Field()
    profitability_ratios_industry_box2 = scrapy.Field()
    profitability_ratios_sector_box2 = scrapy.Field()

    profitability_ratios_name_box3 = scrapy.Field()
    profitability_ratios_company_box3 = scrapy.Field()
    profitability_ratios_industry_box3 = scrapy.Field()
    profitability_ratios_sector_box3 = scrapy.Field()

    profitability_ratios_name_box4 = scrapy.Field()
    profitability_ratios_company_box4 = scrapy.Field()
    profitability_ratios_industry_box4 = scrapy.Field()
    profitability_ratios_sector_box4 = scrapy.Field()

    profitability_ratios_name_box5 = scrapy.Field()
    profitability_ratios_company_box5 = scrapy.Field()
    profitability_ratios_industry_box5 = scrapy.Field()
    profitability_ratios_sector_box5 = scrapy.Field()

    profitability_ratios_name_box6 = scrapy.Field()
    profitability_ratios_company_box6 = scrapy.Field()
    profitability_ratios_industry_box6 = scrapy.Field()
    profitability_ratios_sector_box6 = scrapy.Field()

    profitability_ratios_name_box7 = scrapy.Field()
    profitability_ratios_company_box7 = scrapy.Field()
    profitability_ratios_industry_box7 = scrapy.Field()
    profitability_ratios_sector_box7 = scrapy.Field()

    profitability_ratios_name_box8 = scrapy.Field()
    profitability_ratios_company_box8 = scrapy.Field()
    profitability_ratios_industry_box8 = scrapy.Field()
    profitability_ratios_sector_box8 = scrapy.Field()

    profitability_ratios_name_box9 = scrapy.Field()
    profitability_ratios_company_box9 = scrapy.Field()
    profitability_ratios_industry_box9 = scrapy.Field()
    profitability_ratios_sector_box9 = scrapy.Field()

    profitability_ratios_name_box10 = scrapy.Field()
    profitability_ratios_company_box10 = scrapy.Field()
    profitability_ratios_industry_box10 = scrapy.Field()
    profitability_ratios_sector_box10 = scrapy.Field()

    profitability_ratios_name_box11 = scrapy.Field()
    profitability_ratios_company_box11 = scrapy.Field()
    profitability_ratios_industry_box11 = scrapy.Field()
    profitability_ratios_sector_box11 = scrapy.Field()

    profitability_ratios_name_box12 = scrapy.Field()
    profitability_ratios_company_box12 = scrapy.Field()
    profitability_ratios_industry_box12 = scrapy.Field()
    profitability_ratios_sector_box12 = scrapy.Field()

    # EFFICIENCY
    efficiency_name_box1 = scrapy.Field()
    efficiency_company_box1 = scrapy.Field()
    efficiency_industry_box1 = scrapy.Field()
    efficiency_sector_box1 = scrapy.Field()

    efficiency_name_box2 = scrapy.Field()
    efficiency_company_box2 = scrapy.Field()
    efficiency_industry_box2 = scrapy.Field()
    efficiency_sector_box2 = scrapy.Field()

    efficiency_name_box3 = scrapy.Field()
    efficiency_company_box3 = scrapy.Field()
    efficiency_industry_box3 = scrapy.Field()
    efficiency_sector_box3 = scrapy.Field()

    efficiency_name_box4 = scrapy.Field()
    efficiency_company_box4 = scrapy.Field()
    efficiency_industry_box4 = scrapy.Field()
    efficiency_sector_box4 = scrapy.Field()

    efficiency_name_box5 = scrapy.Field()
    efficiency_company_box5 = scrapy.Field()
    efficiency_industry_box5 = scrapy.Field()
    efficiency_sector_box5 = scrapy.Field()

    # MANAGEMENT EFFECTIVENESS
    management_effectiveness_name_box1 = scrapy.Field()
    management_effectiveness_company_box1 = scrapy.Field()
    management_effectiveness_industry_box1 = scrapy.Field()
    management_effectiveness_sector_box1 = scrapy.Field()

    management_effectiveness_name_box2 = scrapy.Field()
    management_effectiveness_company_box2 = scrapy.Field()
    management_effectiveness_industry_box2 = scrapy.Field()
    management_effectiveness_sector_box2 = scrapy.Field()

    management_effectiveness_name_box3 = scrapy.Field()
    management_effectiveness_company_box3 = scrapy.Field()
    management_effectiveness_industry_box3 = scrapy.Field()
    management_effectiveness_sector_box3 = scrapy.Field()

    management_effectiveness_name_box4 = scrapy.Field()
    management_effectiveness_company_box4 = scrapy.Field()
    management_effectiveness_industry_box4 = scrapy.Field()
    management_effectiveness_sector_box4 = scrapy.Field()

    management_effectiveness_name_box5 = scrapy.Field()
    management_effectiveness_company_box5 = scrapy.Field()
    management_effectiveness_industry_box5 = scrapy.Field()
    management_effectiveness_sector_box5 = scrapy.Field()

    management_effectiveness_name_box6 = scrapy.Field()
    management_effectiveness_company_box6 = scrapy.Field()
    management_effectiveness_industry_box6 = scrapy.Field()
    management_effectiveness_sector_box6 = scrapy.Field()
