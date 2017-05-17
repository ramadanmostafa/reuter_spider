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

def get_consensus_analysis_data(response, item):
    """
    get CONSENSUS ESTIMATES ANALYSIS table
    it will add 45 value to the item then return it
    """
    # initialize the table
    consensus_estimates = [] # estimates, mean, high, low, year_ago
    for index in range(2, 7):
        # will append a column each iteration
        consensus_estimates.append(response.xpath(CONSENSUS_ESTIMATES_XPATH % index).extract())

    # list of tuples to help me construct item keys
    columns_names = [
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
    for index1 in range(5):
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

    return item
