# -*- coding: utf-8 -*-
"""
reuters spider pipeline, insert them to sqlite database
"""
from .reusters_db import ReutersDBInfoTable, ReutersDBConsensusTable, ReutersDBRevenueTable, \
    ReutersDBValuationRatiosTable, ReutersDBDividendsTable, ReutersDBEfficiencyTable, ReutersDBFinancialStrengthTable,\
    ReutersDBGrowthRatesTable, ReutersDBManagementEffectivenessTable, ReutersDBProfitabilityRatiosTable


class ReutersPipeline(object):
    """
    reuters spider item pipeline, used to store scrapped items to sqlite db
    """

    def process_item(self, item, spider):
        """
        cache the scrapped item to the cache json file
        :param item: 
        :param spider: 
        :return: 
        """
        pages_info_table = ReutersDBInfoTable(
            wrong_symbol=item["wrong_symbol"],
            response_status=item["response_status"],
            response_url=item["response_url"],
            symbol=item["symbol"],
            date_scrapped=item["date_scrapped"],
            company_name=item["company_name"],
        )
        if pages_info_table.symbol_in_pages_info_table():
            pages_info_table.update_record_pages_info_table()
        else:
            pages_info_table.insert_record_pages_info_table()

        del pages_info_table
        consensus_table = ReutersDBConsensusTable(
            item["symbol"],
            item["No_consensus_analysis_data_available"],
            item["sales_consensus_box1"],
            item["sales_consensus_box2"],
            item["sales_consensus_box3"],
            item["sales_consensus_box4"],
            item["sales_consensus_box5"],
            item["sales_consensus_box6"],
            item["sales_consensus_box7"],
            item["earning_consensus_box1"],
            item["earning_consensus_box2"],
            item["earning_consensus_box3"],
            item["earning_consensus_box4"],
            item["earning_consensus_box5"],
            item["earning_consensus_box6"],
            item["earning_consensus_box7"],

            item["sales_estimates_box1"],
            item["sales_estimates_box2"],
            item["sales_estimates_box3"],
            item["sales_estimates_box4"],
            item["sales_estimates_box5"],
            item["sales_estimates_box6"],
            item["sales_estimates_box7"],
            item["earning_estimates_box1"],
            item["earning_estimates_box2"],
            item["earning_estimates_box3"],
            item["earning_estimates_box4"],
            item["earning_estimates_box5"],
            item["earning_estimates_box6"],
            item["earning_estimates_box7"],

            item["sales_mean_box1"],
            item["sales_mean_box2"],
            item["sales_mean_box3"],
            item["sales_mean_box4"],
            item["sales_mean_box5"],
            item["sales_mean_box6"],
            item["sales_mean_box7"],
            item["earning_mean_box1"],
            item["earning_mean_box2"],
            item["earning_mean_box3"],
            item["earning_mean_box4"],
            item["earning_mean_box5"],
            item["earning_mean_box6"],
            item["earning_mean_box7"],

            item["sales_high_box1"],
            item["sales_high_box2"],
            item["sales_high_box3"],
            item["sales_high_box4"],
            item["sales_high_box5"],
            item["sales_high_box6"],
            item["sales_high_box7"],
            item["earning_high_box1"],
            item["earning_high_box2"],
            item["earning_high_box3"],
            item["earning_high_box4"],
            item["earning_high_box5"],
            item["earning_high_box6"],
            item["earning_high_box7"],

            item["sales_low_box1"],
            item["sales_low_box2"],
            item["sales_low_box3"],
            item["sales_low_box4"],
            item["sales_low_box5"],
            item["sales_low_box6"],
            item["sales_low_box7"],
            item["earning_low_box1"],
            item["earning_low_box2"],
            item["earning_low_box3"],
            item["earning_low_box4"],
            item["earning_low_box5"],
            item["earning_low_box6"],
            item["earning_low_box7"],

            item["sales_year_ago_box1"],
            item["sales_year_ago_box2"],
            item["sales_year_ago_box3"],
            item["sales_year_ago_box4"],
            item["sales_year_ago_box5"],
            item["sales_year_ago_box6"],
            item["sales_year_ago_box7"],
            item["earning_year_ago_box1"],
            item["earning_year_ago_box2"],
            item["earning_year_ago_box3"],
            item["earning_year_ago_box4"],
            item["earning_year_ago_box5"],
            item["earning_year_ago_box6"],
            item["earning_year_ago_box7"]
        )
        if consensus_table.symbol_in_consensus_table():
            consensus_table.update_record_consensus_table()
        else:
            consensus_table.insert_record_consensus_table()

        del consensus_table

        revenue_table = ReutersDBRevenueTable(
            item["symbol"],
            item["revenue_earnings_per_share_year_box1"],
            item["revenue_earnings_per_share_year_box2"],
            item["revenue_earnings_per_share_year_box3"],
            item["revenue_earnings_per_share_year_box4"],

            item["revenue_earnings_per_share_month_box1"],
            item["revenue_earnings_per_share_month_box2"],
            item["revenue_earnings_per_share_month_box3"],
            item["revenue_earnings_per_share_month_box4"],
            item["revenue_earnings_per_share_month_box5"],
            item["revenue_earnings_per_share_month_box6"],
            item["revenue_earnings_per_share_month_box7"],
            item["revenue_earnings_per_share_month_box8"],
            item["revenue_earnings_per_share_month_box9"],
            item["revenue_earnings_per_share_month_box10"],
            item["revenue_earnings_per_share_month_box11"],
            item["revenue_earnings_per_share_month_box12"],
            item["revenue_earnings_per_share_month_box13"],

            item["revenue_box1"],
            item["revenue_box2"],
            item["revenue_box3"],
            item["revenue_box4"],
            item["revenue_box5"],
            item["revenue_box6"],
            item["revenue_box7"],
            item["revenue_box8"],
            item["revenue_box9"],
            item["revenue_box10"],
            item["revenue_box11"],
            item["revenue_box12"],
            item["revenue_box13"],

            item["earnings_per_share_box1"],
            item["earnings_per_share_box2"],
            item["earnings_per_share_box3"],
            item["earnings_per_share_box4"],
            item["earnings_per_share_box5"],
            item["earnings_per_share_box6"],
            item["earnings_per_share_box7"],
            item["earnings_per_share_box8"],
            item["earnings_per_share_box9"],
            item["earnings_per_share_box10"],
            item["earnings_per_share_box11"],
            item["earnings_per_share_box12"],
            item["earnings_per_share_box1"]
        )
        if revenue_table.symbol_in_revenue_table():
            revenue_table.update_record_revenue_table()
        else:
            revenue_table.insert_record_revenue_table()
        del revenue_table

        valuation_ratios_table = ReutersDBValuationRatiosTable(
            item["symbol"],
            item["valuation_ratios_name_box1"],
            item["valuation_ratios_company_box1"],
            item["valuation_ratios_industry_box1"],
            item["valuation_ratios_sector_box1"],
            item["valuation_ratios_name_box2"],
            item["valuation_ratios_company_box2"],
            item["valuation_ratios_industry_box2"],
            item["valuation_ratios_sector_box2"],
            item["valuation_ratios_name_box3"],
            item["valuation_ratios_company_box3"],
            item["valuation_ratios_industry_box3"],
            item["valuation_ratios_sector_box3"],
            item["valuation_ratios_name_box4"],
            item["valuation_ratios_company_box4"],
            item["valuation_ratios_industry_box4"],
            item["valuation_ratios_sector_box4"],
            item["valuation_ratios_name_box5"],
            item["valuation_ratios_company_box5"],
            item["valuation_ratios_industry_box5"],
            item["valuation_ratios_sector_box5"],
            item["valuation_ratios_name_box6"],
            item["valuation_ratios_company_box6"],
            item["valuation_ratios_industry_box6"],
            item["valuation_ratios_sector_box6"],
            item["valuation_ratios_name_box7"],
            item["valuation_ratios_company_box7"],
            item["valuation_ratios_industry_box7"],
            item["valuation_ratios_sector_box7"],
            item["valuation_ratios_name_box8"],
            item["valuation_ratios_company_box8"],
            item["valuation_ratios_industry_box8"],
            item["valuation_ratios_sector_box8"],
            item["valuation_ratios_name_box9"],
            item["valuation_ratios_company_box9"],
            item["valuation_ratios_industry_box9"],
            item["valuation_ratios_sector_box9"]
        )
        if valuation_ratios_table.symbol_in_valuation_ratios_table():
            valuation_ratios_table.update_record_valuation_ratios_table()
        else:
            valuation_ratios_table.insert_record_valuation_ratios_table()
        del valuation_ratios_table

        dividends_table = ReutersDBDividendsTable(
            item["symbol"],
            item["dividends_name_box1"],
            item["dividends_company_box1"],
            item["dividends_industry_box1"],
            item["dividends_sector_box1"],
            item["dividends_name_box2"],
            item["dividends_company_box2"],
            item["dividends_industry_box2"],
            item["dividends_sector_box2"],
            item["dividends_name_box3"],
            item["dividends_company_box3"],
            item["dividends_industry_box3"],
            item["dividends_sector_box3"],
            item["dividends_name_box4"],
            item["dividends_company_box4"],
            item["dividends_industry_box4"],
            item["dividends_sector_box4"]
        )
        if dividends_table.symbol_in_dividends_table():
            dividends_table.update_record_dividends_table()
        else:
            dividends_table.insert_record_dividends_table()
        del dividends_table

        efficiency_table = ReutersDBEfficiencyTable(
            item["symbol"],
            item["efficiency_name_box1"],
            item["efficiency_company_box1"],
            item["efficiency_industry_box1"],
            item["efficiency_sector_box1"],

            item["efficiency_name_box2"],
            item["efficiency_company_box2"],
            item["efficiency_industry_box2"],
            item["efficiency_sector_box2"],

            item["efficiency_name_box3"],
            item["efficiency_company_box3"],
            item["efficiency_industry_box3"],
            item["efficiency_sector_box3"],

            item["efficiency_name_box4"],
            item["efficiency_company_box4"],
            item["efficiency_industry_box4"],
            item["efficiency_sector_box4"],

            item["efficiency_name_box5"],
            item["efficiency_company_box5"],
            item["efficiency_industry_box5"],
            item["efficiency_sector_box5"]
        )
        if efficiency_table.symbol_in_efficiency_table():
            efficiency_table.update_record_efficiency_table()
        else:
            efficiency_table.insert_record_efficiency_table()

        del efficiency_table

        financial_strength_table = ReutersDBFinancialStrengthTable(
            item["symbol"],
            item["financial_strength_name_box1"],
            item["financial_strength_company_box1"],
            item["financial_strength_industry_box1"],
            item["financial_strength_sector_box1"],

            item["financial_strength_name_box2"],
            item["financial_strength_company_box2"],
            item["financial_strength_industry_box2"],
            item["financial_strength_sector_box2"],

            item["financial_strength_name_box3"],
            item["financial_strength_company_box3"],
            item["financial_strength_industry_box3"],
            item["financial_strength_sector_box3"],

            item["financial_strength_name_box4"],
            item["financial_strength_company_box4"],
            item["financial_strength_industry_box4"],
            item["financial_strength_sector_box4"],

            item["financial_strength_name_box5"],
            item["financial_strength_company_box5"],
            item["financial_strength_industry_box5"],
            item["financial_strength_sector_box5"]
        )
        if financial_strength_table.symbol_in_financial_strength_table():
            financial_strength_table.update_record_financial_strength_table()
        else:
            financial_strength_table.insert_record_financial_strength_table()

        del financial_strength_table

        growth_rates_table = ReutersDBGrowthRatesTable(
            item["symbol"],
            item["growth_rates_name_box1"],
            item["growth_rates_name_box2"],
            item["growth_rates_name_box3"],
            item["growth_rates_name_box4"],
            item["growth_rates_name_box5"],
            item["growth_rates_name_box6"],
            item["growth_rates_name_box7"],

            item["growth_rates_company_box1"],
            item["growth_rates_company_box2"],
            item["growth_rates_company_box3"],
            item["growth_rates_company_box4"],
            item["growth_rates_company_box5"],
            item["growth_rates_company_box6"],
            item["growth_rates_company_box7"],

            item["growth_rates_industry_box1"],
            item["growth_rates_industry_box2"],
            item["growth_rates_industry_box3"],
            item["growth_rates_industry_box4"],
            item["growth_rates_industry_box5"],
            item["growth_rates_industry_box6"],
            item["growth_rates_industry_box7"],

            item["growth_rates_sector_box1"],
            item["growth_rates_sector_box2"],
            item["growth_rates_sector_box3"],
            item["growth_rates_sector_box4"],
            item["growth_rates_sector_box5"],
            item["growth_rates_sector_box6"],
            item["growth_rates_sector_box7"]
        )
        if growth_rates_table.symbol_in_growth_rates_table():
            growth_rates_table.update_record_growth_rates_table()
        else:
            growth_rates_table.insert_record_growth_rates_table()

        del growth_rates_table

        effectiveness_table = ReutersDBManagementEffectivenessTable(
            item["symbol"],
            item["management_effectiveness_name_box1"],
            item["management_effectiveness_company_box1"],
            item["management_effectiveness_industry_box1"],
            item["management_effectiveness_sector_box1"],

            item["management_effectiveness_name_box2"],
            item["management_effectiveness_company_box2"],
            item["management_effectiveness_industry_box2"],
            item["management_effectiveness_sector_box2"],

            item["management_effectiveness_name_box3"],
            item["management_effectiveness_company_box3"],
            item["management_effectiveness_industry_box3"],
            item["management_effectiveness_sector_box3"],

            item["management_effectiveness_name_box4"],
            item["management_effectiveness_company_box4"],
            item["management_effectiveness_industry_box4"],
            item["management_effectiveness_sector_box4"],

            item["management_effectiveness_name_box5"],
            item["management_effectiveness_company_box5"],
            item["management_effectiveness_industry_box5"],
            item["management_effectiveness_sector_box5"],

            item["management_effectiveness_name_box6"],
            item["management_effectiveness_company_box6"],
            item["management_effectiveness_industry_box6"],
            item["management_effectiveness_sector_box6"]
        )
        if effectiveness_table.symbol_in_management_effectiveness_table():
            effectiveness_table.update_record_management_effectiveness_table()
        else:
            effectiveness_table.insert_record_management_effectiveness_table()

        del effectiveness_table

        profitability_ratios_table = ReutersDBProfitabilityRatiosTable(
            item["symbol"],
            item["profitability_ratios_name_box1"],
            item["profitability_ratios_company_box1"],
            item["profitability_ratios_industry_box1"],
            item["profitability_ratios_sector_box1"],

            item["profitability_ratios_name_box2"],
            item["profitability_ratios_company_box2"],
            item["profitability_ratios_industry_box2"],
            item["profitability_ratios_sector_box2"],

            item["profitability_ratios_name_box3"],
            item["profitability_ratios_company_box3"],
            item["profitability_ratios_industry_box3"],
            item["profitability_ratios_sector_box3"],

            item["profitability_ratios_name_box4"],
            item["profitability_ratios_company_box4"],
            item["profitability_ratios_industry_box4"],
            item["profitability_ratios_sector_box4"],

            item["profitability_ratios_name_box5"],
            item["profitability_ratios_company_box5"],
            item["profitability_ratios_industry_box5"],
            item["profitability_ratios_sector_box5"],

            item["profitability_ratios_name_box6"],
            item["profitability_ratios_company_box6"],
            item["profitability_ratios_industry_box6"],
            item["profitability_ratios_sector_box6"],

            item["profitability_ratios_name_box7"],
            item["profitability_ratios_company_box7"],
            item["profitability_ratios_industry_box7"],
            item["profitability_ratios_sector_box7"],

            item["profitability_ratios_name_box8"],
            item["profitability_ratios_company_box8"],
            item["profitability_ratios_industry_box8"],
            item["profitability_ratios_sector_box8"],

            item["profitability_ratios_name_box9"],
            item["profitability_ratios_company_box9"],
            item["profitability_ratios_industry_box9"],
            item["profitability_ratios_sector_box9"],

            item["profitability_ratios_name_box10"],
            item["profitability_ratios_company_box10"],
            item["profitability_ratios_industry_box10"],
            item["profitability_ratios_sector_box10"],

            item["profitability_ratios_name_box11"],
            item["profitability_ratios_company_box11"],
            item["profitability_ratios_industry_box11"],
            item["profitability_ratios_sector_box11"],

            item["profitability_ratios_name_box12"],
            item["profitability_ratios_company_box12"],
            item["profitability_ratios_industry_box12"],
            item["profitability_ratios_sector_box12"]
        )
        if profitability_ratios_table.symbol_in_profitability_ratios_table():
            profitability_ratios_table.update_record_profitability_ratios_table()
        else:
            profitability_ratios_table.insert_record_profitability_ratios_table()

        del profitability_ratios_table
        return item






