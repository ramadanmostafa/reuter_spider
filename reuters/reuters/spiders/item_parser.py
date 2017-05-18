"""
parser for reuters financial page.
if the structure of the pages changed, you need to update this file only.
"""
from ..items import ReutersItem
from datetime import datetime

# constants for xpath rules
COMPANY_NAME_XPATH = '//*[@id="sectionTitle"]/h1/text()'
CONSENSUS_ESTIMATES_IS_AVAILABLE_XPATH = '//*[@id="content"]/div[3]/div/div[2]/div[1]/div[2]/div[2]/text()'
CONSENSUS_ESTIMATES_XPATH = '//*[@id="content"]/div[3]/div/div[2]/div[1]/div[2]/div[2]/table/tbody/tr/td[%d]/text()'
REVENUE_AND_EARNINGS_TABLE_XPATH = '//*[@id="content"]/div[3]/div/div[2]/div[1]/div[1]/div/div/div[2]/table/tbody/tr/td/text()'
VALUATION_RATIOS_DATA_XPATH = '//*[@id="content"]/div[3]/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td/text()'
DIVIDENDS_TABLE_DATA_XPATH = '//*[@id="content"]/div[3]/div/div[2]/div[1]/div[6]/div[2]/table/tbody/tr/td/text()'
GROWTH_RATES_TABLE_XPATH = '//*[@id="content"]/div[3]/div/div[2]/div[1]/div[8]/div[2]/table/tbody/tr/td/text()'
FINANCIAL_STRENGTH_TABLE_XPATH = '//*[@id="content"]/div[3]/div/div[2]/div[1]/div[10]/div[2]/table/tbody/tr/td/text()'
PROFITABILITY_RATIOS_TABLE_XPATH = '//*[@id="content"]/div[3]/div/div[2]/div[1]/div[12]/div[2]/table/tbody/tr/td/text()'
EFFICIENCY_TABLE_XPATH = '//*[@id="content"]/div[3]/div/div[2]/div[1]/div[14]/div[2]/table/tbody/tr/td/text()'
MANAGEMENT_EFFECTIVENESS_TABLE_XPATH = '//*[@id="content"]/div[3]/div/div[2]/div[1]/div[16]/div[2]/table/tbody/tr/td/text()'


def get_consensus_analysis_data(response, item):
    """
    get CONSENSUS ESTIMATES ANALYSIS table
    it will add 45 value to the item then return it
    """
    # initialize the table
    consensus_estimates = [] # estimates, mean, high, low, year_ago
    for index in range(1, 7):
        # will append a column each iteration
        tmp = response.xpath(CONSENSUS_ESTIMATES_XPATH % index).extract()
        if index == 1:
            tmp.pop(0)
            tmp.pop(4)
        consensus_estimates.append(tmp)

    # list of tuples to help me construct item keys
    columns_names = [
        (
            "sales_consensus_box%d",
            "earning_consensus_box%d"
        ),
        (
            "sales_estimates_box%d",
            "earning_estimates_box%d"
        ),
        (
            "sales_mean_box%d",
            "earning_mean_box%d"
        ),
        (
            "sales_high_box%d",
            "earning_high_box%d"
        ),
        (
            "sales_low_box%d",
            "earning_low_box%d"
        ),
        (
            "sales_year_ago_box%d",
            "earning_year_ago_box%d"
        ),
    ]
    # for each column
    for index1 in range(6):
        # for each cell in the column
        for index2 in range(1, 10):
            if index2 < 5:
                # it's sales
                key = columns_names[index1][0] % index2
            else:
                # it's earning
                key = columns_names[index1][1] % (index2 - 4)
            # add data to the item
            item[key] = consensus_estimates[index1][index2 - 1]
    return item


def get_revenue_table_data(response, item):
    """
    get REVENUE & EARNINGS PER SHARE table data
    it will add 33 values to the item
    """
    # get all info in the table
    revenue_table_data = response.xpath(REVENUE_AND_EARNINGS_TABLE_XPATH).extract()
    if len(revenue_table_data) < 1:
        return item

    item["revenue_earnings_per_share_year_box1"] = revenue_table_data[0]
    item["revenue_earnings_per_share_year_box2"] = revenue_table_data[7]
    item["revenue_earnings_per_share_year_box3"] = revenue_table_data[20]

    item["revenue_earnings_per_share_month_box1"] = revenue_table_data[1]
    item["revenue_earnings_per_share_month_box2"] = revenue_table_data[4]
    item["revenue_earnings_per_share_month_box3"] = revenue_table_data[8]
    item["revenue_earnings_per_share_month_box4"] = revenue_table_data[11]
    item["revenue_earnings_per_share_month_box5"] = revenue_table_data[14]
    item["revenue_earnings_per_share_month_box6"] = revenue_table_data[17]
    item["revenue_earnings_per_share_month_box7"] = revenue_table_data[21]
    item["revenue_earnings_per_share_month_box8"] = revenue_table_data[24]
    item["revenue_earnings_per_share_month_box9"] = revenue_table_data[27]
    item["revenue_earnings_per_share_month_box10"] = revenue_table_data[30]

    item["revenue_box1"] = revenue_table_data[2]
    item["revenue_box2"] = revenue_table_data[5]
    item["revenue_box3"] = revenue_table_data[9]
    item["revenue_box4"] = revenue_table_data[12]
    item["revenue_box5"] = revenue_table_data[15]
    item["revenue_box6"] = revenue_table_data[18]
    item["revenue_box7"] = revenue_table_data[22]
    item["revenue_box8"] = revenue_table_data[25]
    item["revenue_box9"] = revenue_table_data[28]
    item["revenue_box10"] = revenue_table_data[31]

    item["earnings_per_share_box1"] = revenue_table_data[3]
    item["earnings_per_share_box2"] = revenue_table_data[6]
    item["earnings_per_share_box3"] = revenue_table_data[10]
    item["earnings_per_share_box4"] = revenue_table_data[13]
    item["earnings_per_share_box5"] = revenue_table_data[16]
    item["earnings_per_share_box6"] = revenue_table_data[19]
    item["earnings_per_share_box7"] = revenue_table_data[23]
    item["earnings_per_share_box8"] = revenue_table_data[26]
    item["earnings_per_share_box9"] = revenue_table_data[29]
    item["earnings_per_share_box10"] = revenue_table_data[32]

    return item


def get_valuation_ratios(response, item):
    """
    get VALUATION RATIOS table data
    it will add 36 values to the item
    """
    valuation_ratios_data = response.xpath(VALUATION_RATIOS_DATA_XPATH).extract()

    if len(valuation_ratios_data) < 1:
        return item

    item["valuation_ratios_name_box1"] = valuation_ratios_data[0]
    item["valuation_ratios_company_box1"] = valuation_ratios_data[1]
    item["valuation_ratios_industry_box1"] = valuation_ratios_data[2]
    item["valuation_ratios_sector_box1"] = valuation_ratios_data[3]

    item["valuation_ratios_name_box2"] = valuation_ratios_data[4]
    item["valuation_ratios_company_box2"] = valuation_ratios_data[5]
    item["valuation_ratios_industry_box2"] = valuation_ratios_data[6]
    item["valuation_ratios_sector_box2"] = valuation_ratios_data[7]

    item["valuation_ratios_name_box3"] = valuation_ratios_data[8]
    item["valuation_ratios_company_box3"] = valuation_ratios_data[9]
    item["valuation_ratios_industry_box3"] = valuation_ratios_data[10]
    item["valuation_ratios_sector_box3"] = valuation_ratios_data[11]

    item["valuation_ratios_name_box4"] = valuation_ratios_data[12]
    item["valuation_ratios_company_box4"] = valuation_ratios_data[13]
    item["valuation_ratios_industry_box4"] = valuation_ratios_data[14]
    item["valuation_ratios_sector_box4"] = valuation_ratios_data[15]

    item["valuation_ratios_name_box5"] = valuation_ratios_data[16]
    item["valuation_ratios_company_box5"] = valuation_ratios_data[17]
    item["valuation_ratios_industry_box5"] = valuation_ratios_data[18]
    item["valuation_ratios_sector_box5"] = valuation_ratios_data[19]

    item["valuation_ratios_name_box6"] = valuation_ratios_data[20]
    item["valuation_ratios_company_box6"] = valuation_ratios_data[21]
    item["valuation_ratios_industry_box6"] = valuation_ratios_data[22]
    item["valuation_ratios_sector_box6"] = valuation_ratios_data[23]

    item["valuation_ratios_name_box7"] = valuation_ratios_data[24]
    item["valuation_ratios_company_box7"] = valuation_ratios_data[25]
    item["valuation_ratios_industry_box7"] = valuation_ratios_data[26]
    item["valuation_ratios_sector_box7"] = valuation_ratios_data[27]

    item["valuation_ratios_name_box8"] = valuation_ratios_data[28]
    item["valuation_ratios_company_box8"] = valuation_ratios_data[29]
    item["valuation_ratios_industry_box8"] = valuation_ratios_data[30]
    item["valuation_ratios_sector_box8"] = valuation_ratios_data[31]

    item["valuation_ratios_name_box9"] = valuation_ratios_data[32]
    item["valuation_ratios_company_box9"] = valuation_ratios_data[33]
    item["valuation_ratios_industry_box9"] = valuation_ratios_data[34]
    item["valuation_ratios_sector_box9"] = valuation_ratios_data[35]

    return item


def get_dividends_data(response, item):
    """
    get DIVIDENDS table data
    it will add 16 values to the item
    """
    dividend_table_data = response.xpath(DIVIDENDS_TABLE_DATA_XPATH).extract()
    if len(dividend_table_data) < 1:
        return item

    item["dividends_name_box1"] = dividend_table_data[0]
    item["dividends_company_box1"] = dividend_table_data[1]
    item["dividends_industry_box1"] = dividend_table_data[2]
    item["dividends_sector_box1"] = dividend_table_data[3]

    item["dividends_name_box2"] = dividend_table_data[4]
    item["dividends_company_box2"] = dividend_table_data[5]
    item["dividends_industry_box2"] = dividend_table_data[6]
    item["dividends_sector_box2"] = dividend_table_data[7]

    item["dividends_name_box3"] = dividend_table_data[8]
    item["dividends_company_box3"] = dividend_table_data[9]
    item["dividends_industry_box3"] = dividend_table_data[10]
    item["dividends_sector_box3"] = dividend_table_data[11]

    item["dividends_name_box4"] = dividend_table_data[12]
    item["dividends_company_box4"] = dividend_table_data[13]
    item["dividends_industry_box4"] = dividend_table_data[14]
    item["dividends_sector_box4"] = dividend_table_data[15]

    return item


def get_growth_rates_date(response, item):
    """
    get growth rates table data
    it will add 28 values to the item
    :param response: 
    :param item: 
    :return: 
    """
    growth_rates_table_data = response.xpath(GROWTH_RATES_TABLE_XPATH).extract()
    if len(growth_rates_table_data) < 1:
        return item

    item["growth_rates_name_box1"] = growth_rates_table_data[0]
    item["growth_rates_name_box2"] = growth_rates_table_data[4]
    item["growth_rates_name_box3"] = growth_rates_table_data[8]
    item["growth_rates_name_box4"] = growth_rates_table_data[12]
    item["growth_rates_name_box5"] = growth_rates_table_data[16]
    item["growth_rates_name_box6"] = growth_rates_table_data[20]
    item["growth_rates_name_box7"] = growth_rates_table_data[24]

    item["growth_rates_company_box1"] = growth_rates_table_data[1]
    item["growth_rates_company_box2"] = growth_rates_table_data[5]
    item["growth_rates_company_box3"] = growth_rates_table_data[9]
    item["growth_rates_company_box4"] = growth_rates_table_data[13]
    item["growth_rates_company_box5"] = growth_rates_table_data[17]
    item["growth_rates_company_box6"] = growth_rates_table_data[21]
    item["growth_rates_company_box7"] = growth_rates_table_data[25]

    item["growth_rates_industry_box1"] = growth_rates_table_data[2]
    item["growth_rates_industry_box2"] = growth_rates_table_data[6]
    item["growth_rates_industry_box3"] = growth_rates_table_data[10]
    item["growth_rates_industry_box4"] = growth_rates_table_data[14]
    item["growth_rates_industry_box5"] = growth_rates_table_data[18]
    item["growth_rates_industry_box6"] = growth_rates_table_data[22]
    item["growth_rates_industry_box7"] = growth_rates_table_data[26]

    item["growth_rates_sector_box1"] = growth_rates_table_data[3]
    item["growth_rates_sector_box2"] = growth_rates_table_data[7]
    item["growth_rates_sector_box3"] = growth_rates_table_data[11]
    item["growth_rates_sector_box4"] = growth_rates_table_data[15]
    item["growth_rates_sector_box5"] = growth_rates_table_data[19]
    item["growth_rates_sector_box6"] = growth_rates_table_data[23]
    item["growth_rates_sector_box7"] = growth_rates_table_data[27]

    return item


def get_financial_strength_table_data(response, item):
    """
    get financial strength table data
    it will add 20 values to the item
    :param response: 
    :param item: 
    :return: 
    """
    financial_strength_table_data = response.xpath(FINANCIAL_STRENGTH_TABLE_XPATH).extract()
    if len(financial_strength_table_data) < 1:
        return item

    item["financial_strength_name_box1"] = financial_strength_table_data[0]
    item["financial_strength_company_box1"] = financial_strength_table_data[1]
    item["financial_strength_industry_box1"] = financial_strength_table_data[2]
    item["financial_strength_sector_box1"] = financial_strength_table_data[3]

    item["financial_strength_name_box2"] = financial_strength_table_data[4]
    item["financial_strength_company_box2"] = financial_strength_table_data[5]
    item["financial_strength_industry_box2"] = financial_strength_table_data[6]
    item["financial_strength_sector_box2"] = financial_strength_table_data[7]

    item["financial_strength_name_box3"] = financial_strength_table_data[8]
    item["financial_strength_company_box3"] = financial_strength_table_data[9]
    item["financial_strength_industry_box3"] = financial_strength_table_data[10]
    item["financial_strength_sector_box3"] = financial_strength_table_data[11]

    item["financial_strength_name_box4"] = financial_strength_table_data[12]
    item["financial_strength_company_box4"] = financial_strength_table_data[13]
    item["financial_strength_industry_box4"] = financial_strength_table_data[14]
    item["financial_strength_sector_box4"] = financial_strength_table_data[15]

    item["financial_strength_name_box5"] = financial_strength_table_data[16]
    item["financial_strength_company_box5"] = financial_strength_table_data[17]
    item["financial_strength_industry_box5"] = financial_strength_table_data[18]
    item["financial_strength_sector_box5"] = financial_strength_table_data[19]

    return item


def get_profitability_ratios_table_data(response, item):
    """
    get profitability ratios table data
    it will add 48 values to the item
    :param response: 
    :param item: 
    :return: 
    """
    profitability_ratios_table_data = response.xpath(PROFITABILITY_RATIOS_TABLE_XPATH).extract()
    if len(profitability_ratios_table_data) < 1:
        return item

    item["profitability_ratios_name_box1"] = profitability_ratios_table_data[0]
    item["profitability_ratios_company_box1"] = profitability_ratios_table_data[1]
    item["profitability_ratios_industry_box1"] = profitability_ratios_table_data[2]
    item["profitability_ratios_sector_box1"] = profitability_ratios_table_data[3]

    item["profitability_ratios_name_box2"] = profitability_ratios_table_data[4]
    item["profitability_ratios_company_box2"] = profitability_ratios_table_data[5]
    item["profitability_ratios_industry_box2"] = profitability_ratios_table_data[6]
    item["profitability_ratios_sector_box2"] = profitability_ratios_table_data[7]

    item["profitability_ratios_name_box3"] = profitability_ratios_table_data[8]
    item["profitability_ratios_company_box3"] = profitability_ratios_table_data[9]
    item["profitability_ratios_industry_box3"] = profitability_ratios_table_data[10]
    item["profitability_ratios_sector_box3"] = profitability_ratios_table_data[11]

    item["profitability_ratios_name_box4"] = profitability_ratios_table_data[12]
    item["profitability_ratios_company_box4"] = profitability_ratios_table_data[13]
    item["profitability_ratios_industry_box4"] = profitability_ratios_table_data[14]
    item["profitability_ratios_sector_box4"] = profitability_ratios_table_data[15]

    item["profitability_ratios_name_box5"] = profitability_ratios_table_data[16]
    item["profitability_ratios_company_box5"] = profitability_ratios_table_data[17]
    item["profitability_ratios_industry_box5"] = profitability_ratios_table_data[18]
    item["profitability_ratios_sector_box5"] = profitability_ratios_table_data[19]

    item["profitability_ratios_name_box6"] = profitability_ratios_table_data[20]
    item["profitability_ratios_company_box6"] = profitability_ratios_table_data[21]
    item["profitability_ratios_industry_box6"] = profitability_ratios_table_data[22]
    item["profitability_ratios_sector_box6"] = profitability_ratios_table_data[23]

    item["profitability_ratios_name_box7"] = profitability_ratios_table_data[24]
    item["profitability_ratios_company_box7"] = profitability_ratios_table_data[25]
    item["profitability_ratios_industry_box7"] = profitability_ratios_table_data[26]
    item["profitability_ratios_sector_box7"] = profitability_ratios_table_data[27]

    item["profitability_ratios_name_box8"] = profitability_ratios_table_data[28]
    item["profitability_ratios_company_box8"] = profitability_ratios_table_data[29]
    item["profitability_ratios_industry_box8"] = profitability_ratios_table_data[30]
    item["profitability_ratios_sector_box8"] = profitability_ratios_table_data[31]

    item["profitability_ratios_name_box9"] = profitability_ratios_table_data[32]
    item["profitability_ratios_company_box9"] = profitability_ratios_table_data[33]
    item["profitability_ratios_industry_box9"] = profitability_ratios_table_data[34]
    item["profitability_ratios_sector_box9"] = profitability_ratios_table_data[35]

    item["profitability_ratios_name_box10"] = profitability_ratios_table_data[36]
    item["profitability_ratios_company_box10"] = profitability_ratios_table_data[37]
    item["profitability_ratios_industry_box10"] = profitability_ratios_table_data[38]
    item["profitability_ratios_sector_box10"] = profitability_ratios_table_data[39]

    item["profitability_ratios_name_box11"] = profitability_ratios_table_data[40]
    item["profitability_ratios_company_box11"] = profitability_ratios_table_data[41]
    item["profitability_ratios_industry_box11"] = profitability_ratios_table_data[42]
    item["profitability_ratios_sector_box11"] = profitability_ratios_table_data[43]

    item["profitability_ratios_name_box12"] = profitability_ratios_table_data[44]
    item["profitability_ratios_company_box12"] = profitability_ratios_table_data[45]
    item["profitability_ratios_industry_box12"] = profitability_ratios_table_data[46]
    item["profitability_ratios_sector_box12"] = profitability_ratios_table_data[47]

    return item


def get_efficiency_table_data(response, item):
    """
    get efficiency table data
    it will add 20 values to the item
    :param response: 
    :param item: 
    :return: 
    """
    efficiency_table_data = response.xpath(EFFICIENCY_TABLE_XPATH).extract()
    if len(efficiency_table_data) < 1:
        return item

    item["efficiency_name_box1"] = efficiency_table_data[0]
    item["efficiency_company_box1"] = efficiency_table_data[1]
    item["efficiency_industry_box1"] = efficiency_table_data[2]
    item["efficiency_sector_box1"] = efficiency_table_data[3]

    item["efficiency_name_box2"] = efficiency_table_data[4]
    item["efficiency_company_box2"] = efficiency_table_data[5]
    item["efficiency_industry_box2"] = efficiency_table_data[6]
    item["efficiency_sector_box2"] = efficiency_table_data[7]

    item["efficiency_name_box3"] = efficiency_table_data[8]
    item["efficiency_company_box3"] = efficiency_table_data[9]
    item["efficiency_industry_box3"] = efficiency_table_data[10]
    item["efficiency_sector_box3"] = efficiency_table_data[11]

    item["efficiency_name_box4"] = efficiency_table_data[12]
    item["efficiency_company_box4"] = efficiency_table_data[13]
    item["efficiency_industry_box4"] = efficiency_table_data[14]
    item["efficiency_sector_box4"] = efficiency_table_data[15]

    item["efficiency_name_box5"] = efficiency_table_data[16]
    item["efficiency_company_box5"] = efficiency_table_data[17]
    item["efficiency_industry_box5"] = efficiency_table_data[18]
    item["efficiency_sector_box5"] = efficiency_table_data[19]

    return item


def get_management_effectiveness_table_data(response, item):
    """
    get management effectiveness table data
    it will add 24 values to the item
    :param response: 
    :param item: 
    :return: 
    """
    management_effectiveness_table_data = response.xpath(MANAGEMENT_EFFECTIVENESS_TABLE_XPATH).extract()
    if len(management_effectiveness_table_data) < 1:
        return item

    item["management_effectiveness_name_box1"] = management_effectiveness_table_data[0]
    item["management_effectiveness_company_box1"] = management_effectiveness_table_data[1]
    item["management_effectiveness_industry_box1"] = management_effectiveness_table_data[2]
    item["management_effectiveness_sector_box1"] = management_effectiveness_table_data[3]

    item["management_effectiveness_name_box2"] = management_effectiveness_table_data[4]
    item["management_effectiveness_company_box2"] = management_effectiveness_table_data[5]
    item["management_effectiveness_industry_box2"] = management_effectiveness_table_data[6]
    item["management_effectiveness_sector_box2"] = management_effectiveness_table_data[7]

    item["management_effectiveness_name_box3"] = management_effectiveness_table_data[8]
    item["management_effectiveness_company_box3"] = management_effectiveness_table_data[9]
    item["management_effectiveness_industry_box3"] = management_effectiveness_table_data[10]
    item["management_effectiveness_sector_box3"] = management_effectiveness_table_data[11]

    item["management_effectiveness_name_box4"] = management_effectiveness_table_data[12]
    item["management_effectiveness_company_box4"] = management_effectiveness_table_data[13]
    item["management_effectiveness_industry_box4"] = management_effectiveness_table_data[14]
    item["management_effectiveness_sector_box4"] = management_effectiveness_table_data[15]

    item["management_effectiveness_name_box5"] = management_effectiveness_table_data[16]
    item["management_effectiveness_company_box5"] = management_effectiveness_table_data[17]
    item["management_effectiveness_industry_box5"] = management_effectiveness_table_data[18]
    item["management_effectiveness_sector_box5"] = management_effectiveness_table_data[19]

    item["management_effectiveness_name_box6"] = management_effectiveness_table_data[20]
    item["management_effectiveness_company_box6"] = management_effectiveness_table_data[21]
    item["management_effectiveness_industry_box6"] = management_effectiveness_table_data[22]
    item["management_effectiveness_sector_box6"] = management_effectiveness_table_data[23]

    return item


def financial_parser(response):
    """
    take the response from reuter_spider and return a ReutersItem
    """
    item = ReutersItem()
    item["wrong_symbol"] = False
    item["response_status"] = response.status
    item["response_url"] = response.url
    item["symbol"] = response.url.split("=")[-1]
    item["date_scrapped"] = str(datetime.now().date())
    item["company_name"] = response.xpath(COMPANY_NAME_XPATH).extract_first()
    item["No_consensus_analysis_data_available"] = True
    if item["company_name"] is None:
        item["wrong_symbol"] = True
    else:
        if response.xpath(CONSENSUS_ESTIMATES_IS_AVAILABLE_XPATH).extract_first().strip() == '':
            # CONSENSUS ESTIMATES ANALYSIS table is available in the page
            item["No_consensus_analysis_data_available"] = False
            item = get_consensus_analysis_data(response, item)
        item = get_revenue_table_data(response, item)
        item = get_valuation_ratios(response, item)
        item = get_dividends_data(response, item)
        item = get_growth_rates_date(response, item)
        item = get_financial_strength_table_data(response, item)
        item = get_profitability_ratios_table_data(response, item)
        item = get_efficiency_table_data(response, item)
        item = get_management_effectiveness_table_data(response, item)

    return item
