"""
parser for reuter financial page.
if the strucure of the pages changed, you need to update this file only.
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
    it will add 2 value to the item
    """
    # get all info in the table
    revenue_table_data = response.xpath(REVENUE_AND_EARNINGS_TABLE_XPATH).extract()
    # init item
    item["revenue"] = []
    item["earnings_per_share"] = []
    # if flag is True --> this number is revenue
    # if flag is False --> this number is earnings_per_share
    flag = True
    for record in revenue_table_data:
        # check if the current data is all digits
        if record.replace(',', '').replace('.', '').isdigit():
            if flag:
                item["revenue"].append(record)
                flag = False
            else:
                item["earnings_per_share"].append(record)
                flag = True
    return item

def get_valuation_ratios(response, item):
    """
    get VALUATION RATIOS table data
    it will add 27 value to the item
    """
    valuation_ratios_data = response.xpath(VALUATION_RATIOS_DATA_XPATH).extract()

    item["P_E_Ratio_TTM_Company"] = valuation_ratios_data[1]
    item["P_E_High_Company"] = valuation_ratios_data[5]
    item["P_E_Low_Company"] = valuation_ratios_data[9]
    item["Beta_Company"] = valuation_ratios_data[13]
    item["Price_to_Sales_TTM_Company"] = valuation_ratios_data[17]
    item["Price_to_Book_MRQ_Company"] = valuation_ratios_data[21]
    item["Price_to_Tangible_Book_MRQ_Company"] = valuation_ratios_data[25]
    item["Price_to_Cash_Flow_TTM_Company"] = valuation_ratios_data[29]
    item["Owned_Institutions_Company"] = valuation_ratios_data[33]

    item["P_E_Ratio_TTM_industry"] = valuation_ratios_data[2]
    item["P_E_High_industry"] = valuation_ratios_data[6]
    item["P_E_Low_industry"] = valuation_ratios_data[10]
    item["Beta_industry"] = valuation_ratios_data[14]
    item["Price_to_Sales_TTM_industry"] = valuation_ratios_data[18]
    item["Price_to_Book_MRQ_industry"] = valuation_ratios_data[22]
    item["Price_to_Tangible_Book_MRQ_industry"] = valuation_ratios_data[26]
    item["Price_to_Cash_Flow_TTM_industry"] = valuation_ratios_data[30]
    item["Owned_Institutions_industry"] = valuation_ratios_data[34]

    item["P_E_Ratio_TTM_sector"] = valuation_ratios_data[3]
    item["P_E_High_sector"] = valuation_ratios_data[7]
    item["P_E_Low_sector"] = valuation_ratios_data[11]
    item["Beta_sector"] = valuation_ratios_data[15]
    item["Price_to_Sales_TTM_sector"] = valuation_ratios_data[19]
    item["Price_to_Book_MRQ_sector"] = valuation_ratios_data[23]
    item["Price_to_Tangible_Book_MRQ_sector"] = valuation_ratios_data[27]
    item["Price_to_Cash_Flow_TTM_sector"] = valuation_ratios_data[31]
    item["Owned_Institutions_sector"] = valuation_ratios_data[35]
    return item

def get_dividends_data(response, item):
    """
    get DIVIDENDS table data
    it will add 12 value to the item
    """
    dividend_table_data = response.xpath(DIVIDENDS_TABLE_DATA_XPATH).extract()

    item["Dividend_Yield_Company"] = dividend_table_data[1]
    item["Dividend_Yield_five_Year_Avg_Company"] = dividend_table_data[5]
    item["Dividend_five_Year_Growth_Rate_Company"] = dividend_table_data[9]
    item["Payout_Ratio_TTM_Company"] = dividend_table_data[13]

    item["Dividend_Yield_industry"] = dividend_table_data[2]
    item["Dividend_Yield_five_Year_Avg_industry"] = dividend_table_data[6]
    item["Dividend_five_Year_Growth_Rate_industry"] = dividend_table_data[10]
    item["Payout_Ratio_TTM_industry"] = dividend_table_data[14]

    item["Dividend_Yield_sector"] = dividend_table_data[3]
    item["Dividend_Yield_five_Year_Avg_sector"] = dividend_table_data[7]
    item["Dividend_five_Year_Growth_Rate_sector"] = dividend_table_data[11]
    item["Payout_Ratio_TTM_sector"] = dividend_table_data[15]

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



    return item
