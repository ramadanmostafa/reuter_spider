"""
class to interact with the database
"""
import sqlite3
from scrapy.conf import settings


class ReutersDBConnection(object):
    """
    parent class of the database classes, contains the shared methods
    """

    def _connect(self):
        """
        connect to the sqlite database and return the connection
        :rtype: sqlite db connection
        """
        try:
            con = sqlite3.connect(settings.get('DATABASE_NAME'))
            return con
        except:
            raise RuntimeError("An Exception happened with the Database, make sure you are connected")


class ReutersDBInfoTable(ReutersDBConnection):
    """
    insert, update, select and delete from info_pages table
    """
    def __init__(self, response_status, response_url, symbol, date_scrapped, company_name, wrong_symbol):
        self.response_status = response_status
        self.response_url = response_url
        self.symbol = symbol
        self.date_scrapped = date_scrapped
        self.company_name = company_name
        self.wrong_symbol = wrong_symbol

    def insert_record_pages_info_table(self):

        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            insert into pages_info (
              company_name,
              date_scrapped,
              response_status,
              response_url,
              symbol,
              wrong_symbol
            )
            values (?, ?, ?, ?, ?, ?)
        """
        cur.execute(
            sql_query, (
                self.company_name,
                self.date_scrapped,
                self.response_status,
                self.response_url,
                self.symbol,
                self.wrong_symbol
            )
        )
        conn.commit()
        conn.close()

    def update_record_pages_info_table(self):

        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            update pages_info
            set company_name=?,
                date_scrapped=?,
                response_status=?,
                response_url=?,
                wrong_symbol=?
            where symbol=?
        """
        cur.execute(
            sql_query, (
                self.company_name,
                self.date_scrapped,
                self.response_status,
                self.response_url,
                self.wrong_symbol,
                self.symbol
            )
        )
        conn.commit()
        conn.close()

    def symbol_in_pages_info_table(self):
        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            select id from pages_info where pages_info.symbol=?
        """
        cur.execute(sql_query, (self.symbol,))
        rows_count = len(cur.fetchall())
        conn.close()
        return rows_count == 1


class ReutersDBConsensusTable(ReutersDBConnection):

    def __init__(
        self,
        symbol,
        No_consensus_analysis_data_available,
        sales_consensus_box1,
        sales_consensus_box2,
        sales_consensus_box3,
        sales_consensus_box4,
        sales_consensus_box5,
        sales_consensus_box6,
        sales_consensus_box7,
        earning_consensus_box1,
        earning_consensus_box2,
        earning_consensus_box3,
        earning_consensus_box4,
        earning_consensus_box5,
        earning_consensus_box6,
        earning_consensus_box7,

        sales_estimates_box1,
        sales_estimates_box2,
        sales_estimates_box3,
        sales_estimates_box4,
        sales_estimates_box5,
        sales_estimates_box6,
        sales_estimates_box7,
        earning_estimates_box1,
        earning_estimates_box2,
        earning_estimates_box3,
        earning_estimates_box4,
        earning_estimates_box5,
        earning_estimates_box6,
        earning_estimates_box7,

        sales_mean_box1,
        sales_mean_box2,
        sales_mean_box3,
        sales_mean_box4,
        sales_mean_box5,
        sales_mean_box6,
        sales_mean_box7,
        earning_mean_box1,
        earning_mean_box2,
        earning_mean_box3,
        earning_mean_box4,
        earning_mean_box5,
        earning_mean_box6,
        earning_mean_box7,

        sales_high_box1,
        sales_high_box2,
        sales_high_box3,
        sales_high_box4,
        sales_high_box5,
        sales_high_box6,
        sales_high_box7,
        earning_high_box1,
        earning_high_box2,
        earning_high_box3,
        earning_high_box4,
        earning_high_box5,
        earning_high_box6,
        earning_high_box7,

        sales_low_box1,
        sales_low_box2,
        sales_low_box3,
        sales_low_box4,
        sales_low_box5,
        sales_low_box6,
        sales_low_box7,
        earning_low_box1,
        earning_low_box2,
        earning_low_box3,
        earning_low_box4,
        earning_low_box5,
        earning_low_box6,
        earning_low_box7,

        sales_year_ago_box1,
        sales_year_ago_box2,
        sales_year_ago_box3,
        sales_year_ago_box4,
        sales_year_ago_box5,
        sales_year_ago_box6,
        sales_year_ago_box7,
        earning_year_ago_box1,
        earning_year_ago_box2,
        earning_year_ago_box3,
        earning_year_ago_box4,
        earning_year_ago_box5,
        earning_year_ago_box6,
        earning_year_ago_box7,
        date_scrapped
    ):
        self.symbol = symbol
        self.No_consensus_analysis_data_available = No_consensus_analysis_data_available
        self.sales_consensus_box1 = sales_consensus_box1
        self.sales_consensus_box2 = sales_consensus_box2
        self.sales_consensus_box3 = sales_consensus_box3
        self.sales_consensus_box4 = sales_consensus_box4
        self.sales_consensus_box5 = sales_consensus_box5
        self.sales_consensus_box6 = sales_consensus_box6
        self.sales_consensus_box7 = sales_consensus_box7
        self.earning_consensus_box1 = earning_consensus_box1
        self.earning_consensus_box2 = earning_consensus_box2
        self.earning_consensus_box3 = earning_consensus_box3
        self.earning_consensus_box4 = earning_consensus_box4
        self.earning_consensus_box5 = earning_consensus_box5
        self.earning_consensus_box6 = earning_consensus_box6
        self.earning_consensus_box7 = earning_consensus_box7

        self.sales_estimates_box1 = sales_estimates_box1
        self.sales_estimates_box2 = sales_estimates_box2
        self.sales_estimates_box3 = sales_estimates_box3
        self.sales_estimates_box4 = sales_estimates_box4
        self.sales_estimates_box5 = sales_estimates_box5
        self.sales_estimates_box6 = sales_estimates_box6
        self.sales_estimates_box7 = sales_estimates_box7
        self.earning_estimates_box1 = earning_estimates_box1
        self.earning_estimates_box2 = earning_estimates_box2
        self.earning_estimates_box3 = earning_estimates_box3
        self.earning_estimates_box4 = earning_estimates_box4
        self.earning_estimates_box5 = earning_estimates_box5
        self.earning_estimates_box6 = earning_estimates_box6
        self.earning_estimates_box7 = earning_estimates_box7

        self.sales_mean_box1 = sales_mean_box1
        self.sales_mean_box2 = sales_mean_box2
        self.sales_mean_box3 = sales_mean_box3
        self.sales_mean_box4 = sales_mean_box4
        self.sales_mean_box5 = sales_mean_box5
        self.sales_mean_box6 = sales_mean_box6
        self.sales_mean_box7 = sales_mean_box7
        self.earning_mean_box1 = earning_mean_box1
        self.earning_mean_box2 = earning_mean_box2
        self.earning_mean_box3 = earning_mean_box3
        self.earning_mean_box4 = earning_mean_box4
        self.earning_mean_box5 = earning_mean_box5
        self.earning_mean_box6 = earning_mean_box6
        self.earning_mean_box7 = earning_mean_box7

        self.sales_high_box1 = sales_high_box1
        self.sales_high_box2 = sales_high_box2
        self.sales_high_box3 = sales_high_box3
        self.sales_high_box4 = sales_high_box4
        self.sales_high_box5 = sales_high_box5
        self.sales_high_box6 = sales_high_box6
        self.sales_high_box7 = sales_high_box7
        self.earning_high_box1 = earning_high_box1
        self.earning_high_box2 = earning_high_box2
        self.earning_high_box3 = earning_high_box3
        self.earning_high_box4 = earning_high_box4
        self.earning_high_box5 = earning_high_box5
        self.earning_high_box6 = earning_high_box6
        self.earning_high_box7 = earning_high_box7

        self.sales_low_box1 = sales_low_box1
        self.sales_low_box2 = sales_low_box2
        self.sales_low_box3 = sales_low_box3
        self.sales_low_box4 = sales_low_box4
        self.sales_low_box5 = sales_low_box5
        self.sales_low_box6 = sales_low_box6
        self.sales_low_box7 = sales_low_box7
        self.earning_low_box1 = earning_low_box1
        self.earning_low_box2 = earning_low_box2
        self.earning_low_box3 = earning_low_box3
        self.earning_low_box4 = earning_low_box4
        self.earning_low_box5 = earning_low_box5
        self.earning_low_box6 = earning_low_box6
        self.earning_low_box7 = earning_low_box7

        self.sales_year_ago_box1 = sales_year_ago_box1
        self.sales_year_ago_box2 = sales_year_ago_box2
        self.sales_year_ago_box3 = sales_year_ago_box3
        self.sales_year_ago_box4 = sales_year_ago_box4
        self.sales_year_ago_box5 = sales_year_ago_box5
        self.sales_year_ago_box6 = sales_year_ago_box6
        self.sales_year_ago_box7 = sales_year_ago_box7
        self.earning_year_ago_box1 = earning_year_ago_box1
        self.earning_year_ago_box2 = earning_year_ago_box2
        self.earning_year_ago_box3 = earning_year_ago_box3
        self.earning_year_ago_box4 = earning_year_ago_box4
        self.earning_year_ago_box5 = earning_year_ago_box5
        self.earning_year_ago_box6 = earning_year_ago_box6
        self.earning_year_ago_box7 = earning_year_ago_box7
        self.date_scrapped = date_scrapped


    def insert_record_consensus_table(self):
        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
                    insert into consensus_analysis_data (
                        symbol,
                        No_consensus_analysis_data_available,
                        sales_consensus_box1,
                        sales_consensus_box2,
                        sales_consensus_box3,
                        sales_consensus_box4,
                        sales_consensus_box5,
                        sales_consensus_box6,
                        sales_consensus_box7,
                        earning_consensus_box1,
                        earning_consensus_box2,
                        earning_consensus_box3,
                        earning_consensus_box4,
                        earning_consensus_box5,
                        earning_consensus_box6,
                        earning_consensus_box7,
                        sales_estimates_box1,
                        sales_estimates_box2,
                        sales_estimates_box3,
                        sales_estimates_box4,
                        sales_estimates_box5,
                        sales_estimates_box6,
                        sales_estimates_box7,
                        earning_estimates_box1,
                        earning_estimates_box2,
                        earning_estimates_box3,
                        earning_estimates_box4,
                        earning_estimates_box5,
                        earning_estimates_box6,
                        earning_estimates_box7,
                        sales_mean_box1,
                        sales_mean_box2,
                        sales_mean_box3,
                        sales_mean_box4,
                        sales_mean_box5,
                        sales_mean_box6,
                        sales_mean_box7,
                        earning_mean_box1,
                        earning_mean_box2,
                        earning_mean_box3,
                        earning_mean_box4,
                        earning_mean_box5,
                        earning_mean_box6,
                        earning_mean_box7,
                        sales_high_box1,
                        sales_high_box2,
                        sales_high_box3,
                        sales_high_box4,
                        sales_high_box5,
                        sales_high_box6,
                        sales_high_box7,
                        earning_high_box1,
                        earning_high_box2,
                        earning_high_box3,
                        earning_high_box4,
                        earning_high_box5,
                        earning_high_box6,
                        earning_high_box7,
                        sales_low_box1,
                        sales_low_box2,
                        sales_low_box3,
                        sales_low_box4,
                        sales_low_box5,
                        sales_low_box6,
                        sales_low_box7,
                        earning_low_box1,
                        earning_low_box2,
                        earning_low_box3,
                        earning_low_box4,
                        earning_low_box5,
                        earning_low_box6,
                        earning_low_box7,
                        sales_year_ago_box1,
                        sales_year_ago_box2,
                        sales_year_ago_box3,
                        sales_year_ago_box4,
                        sales_year_ago_box5,
                        sales_year_ago_box6,
                        sales_year_ago_box7,
                        earning_year_ago_box1,
                        earning_year_ago_box2,
                        earning_year_ago_box3,
                        earning_year_ago_box4,
                        earning_year_ago_box5,
                        earning_year_ago_box6,
                        earning_year_ago_box7,
                        date_scrapped

                    )
                    values (
                    ?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?,?
                    )
                """
        cur.execute(
            sql_query, (
                self.symbol,
                self.No_consensus_analysis_data_available,
                self.sales_consensus_box1,
                self.sales_consensus_box2,
                self.sales_consensus_box3,
                self.sales_consensus_box4,
                self.sales_consensus_box5,
                self.sales_consensus_box6,
                self.sales_consensus_box7,
                self.earning_consensus_box1,
                self.earning_consensus_box2,
                self.earning_consensus_box3,
                self.earning_consensus_box4,
                self.earning_consensus_box5,
                self.earning_consensus_box6,
                self.earning_consensus_box7,
                self.sales_estimates_box1,
                self.sales_estimates_box2,
                self.sales_estimates_box3,
                self.sales_estimates_box4,
                self.sales_estimates_box5,
                self.sales_estimates_box6,
                self.sales_estimates_box7,
                self.earning_estimates_box1,
                self.earning_estimates_box2,
                self.earning_estimates_box3,
                self.earning_estimates_box4,
                self.earning_estimates_box5,
                self.earning_estimates_box6,
                self.earning_estimates_box7,
                self.sales_mean_box1,
                self.sales_mean_box2,
                self.sales_mean_box3,
                self.sales_mean_box4,
                self.sales_mean_box5,
                self.sales_mean_box6,
                self.sales_mean_box7,
                self.earning_mean_box1,
                self.earning_mean_box2,
                self.earning_mean_box3,
                self.earning_mean_box4,
                self.earning_mean_box5,
                self.earning_mean_box6,
                self.earning_mean_box7,
                self.sales_high_box1,
                self.sales_high_box2,
                self.sales_high_box3,
                self.sales_high_box4,
                self.sales_high_box5,
                self.sales_high_box6,
                self.sales_high_box7,
                self.earning_high_box1,
                self.earning_high_box2,
                self.earning_high_box3,
                self.earning_high_box4,
                self.earning_high_box5,
                self.earning_high_box6,
                self.earning_high_box7,
                self.sales_low_box1,
                self.sales_low_box2,
                self.sales_low_box3,
                self.sales_low_box4,
                self.sales_low_box5,
                self.sales_low_box6,
                self.sales_low_box7,
                self.earning_low_box1,
                self.earning_low_box2,
                self.earning_low_box3,
                self.earning_low_box4,
                self.earning_low_box5,
                self.earning_low_box6,
                self.earning_low_box7,
                self.sales_year_ago_box1,
                self.sales_year_ago_box2,
                self.sales_year_ago_box3,
                self.sales_year_ago_box4,
                self.sales_year_ago_box5,
                self.sales_year_ago_box6,
                self.sales_year_ago_box7,
                self.earning_year_ago_box1,
                self.earning_year_ago_box2,
                self.earning_year_ago_box3,
                self.earning_year_ago_box4,
                self.earning_year_ago_box5,
                self.earning_year_ago_box6,
                self.earning_year_ago_box7,
                self.date_scrapped
            )
        )
        conn.commit()
        conn.close()

    def update_record_consensus_table(self):
        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
                    update consensus_analysis_data
                    set No_consensus_analysis_data_available=?,
                        sales_consensus_box1=?,
                        sales_consensus_box2=?,
                        sales_consensus_box3=?,
                        sales_consensus_box4=?,
                        sales_consensus_box5=?,
                        sales_consensus_box6=?,
                        sales_consensus_box7=?,
                        earning_consensus_box1=?,
                        earning_consensus_box2=?,
                        earning_consensus_box3=?,
                        earning_consensus_box4=?,
                        earning_consensus_box5=?,
                        earning_consensus_box6=?,
                        earning_consensus_box7=?,
                        sales_estimates_box1=?,
                        sales_estimates_box2=?,
                        sales_estimates_box3=?,
                        sales_estimates_box4=?,
                        sales_estimates_box5=?,
                        sales_estimates_box6=?,
                        sales_estimates_box7=?,
                        earning_estimates_box1=?,
                        earning_estimates_box2=?,
                        earning_estimates_box3=?,
                        earning_estimates_box4=?,
                        earning_estimates_box5=?,
                        earning_estimates_box6=?,
                        earning_estimates_box7=?,
                        sales_mean_box1=?,
                        sales_mean_box2=?,
                        sales_mean_box3=?,
                        sales_mean_box4=?,
                        sales_mean_box5=?,
                        sales_mean_box6=?,
                        sales_mean_box7=?,
                        earning_mean_box1=?,
                        earning_mean_box2=?,
                        earning_mean_box3=?,
                        earning_mean_box4=?,
                        earning_mean_box5=?,
                        earning_mean_box6=?,
                        earning_mean_box7=?,
                        sales_high_box1=?,
                        sales_high_box2=?,
                        sales_high_box3=?,
                        sales_high_box4=?,
                        sales_high_box5=?,
                        sales_high_box6=?,
                        sales_high_box7=?,
                        earning_high_box1=?,
                        earning_high_box2=?,
                        earning_high_box3=?,
                        earning_high_box4=?,
                        earning_high_box5=?,
                        earning_high_box6=?,
                        earning_high_box7=?,
                        sales_low_box1=?,
                        sales_low_box2=?,
                        sales_low_box3=?,
                        sales_low_box4=?,
                        sales_low_box5=?,
                        sales_low_box6=?,
                        sales_low_box7=?,
                        earning_low_box1=?,
                        earning_low_box2=?,
                        earning_low_box3=?,
                        earning_low_box4=?,
                        earning_low_box5=?,
                        earning_low_box6=?,
                        earning_low_box7=?,
                        sales_year_ago_box1=?,
                        sales_year_ago_box2=?,
                        sales_year_ago_box3=?,
                        sales_year_ago_box4=?,
                        sales_year_ago_box5=?,
                        sales_year_ago_box6=?,
                        sales_year_ago_box7=?,
                        earning_year_ago_box1=?,
                        earning_year_ago_box2=?,
                        earning_year_ago_box3=?,
                        earning_year_ago_box4=?,
                        earning_year_ago_box5=?,
                        earning_year_ago_box6=?,
                        earning_year_ago_box7=?
                    where symbol=?
                """
        cur.execute(
            sql_query, (
                self.No_consensus_analysis_data_available,
                self.sales_consensus_box1,
                self.sales_consensus_box2,
                self.sales_consensus_box3,
                self.sales_consensus_box4,
                self.sales_consensus_box5,
                self.sales_consensus_box6,
                self.sales_consensus_box7,
                self.earning_consensus_box1,
                self.earning_consensus_box2,
                self.earning_consensus_box3,
                self.earning_consensus_box4,
                self.earning_consensus_box5,
                self.earning_consensus_box6,
                self.earning_consensus_box7,
                self.sales_estimates_box1,
                self.sales_estimates_box2,
                self.sales_estimates_box3,
                self.sales_estimates_box4,
                self.sales_estimates_box5,
                self.sales_estimates_box6,
                self.sales_estimates_box7,
                self.earning_estimates_box1,
                self.earning_estimates_box2,
                self.earning_estimates_box3,
                self.earning_estimates_box4,
                self.earning_estimates_box5,
                self.earning_estimates_box6,
                self.earning_estimates_box7,
                self.sales_mean_box1,
                self.sales_mean_box2,
                self.sales_mean_box3,
                self.sales_mean_box4,
                self.sales_mean_box5,
                self.sales_mean_box6,
                self.sales_mean_box7,
                self.earning_mean_box1,
                self.earning_mean_box2,
                self.earning_mean_box3,
                self.earning_mean_box4,
                self.earning_mean_box5,
                self.earning_mean_box6,
                self.earning_mean_box7,
                self.sales_high_box1,
                self.sales_high_box2,
                self.sales_high_box3,
                self.sales_high_box4,
                self.sales_high_box5,
                self.sales_high_box6,
                self.sales_high_box7,
                self.earning_high_box1,
                self.earning_high_box2,
                self.earning_high_box3,
                self.earning_high_box4,
                self.earning_high_box5,
                self.earning_high_box6,
                self.earning_high_box7,
                self.sales_low_box1,
                self.sales_low_box2,
                self.sales_low_box3,
                self.sales_low_box4,
                self.sales_low_box5,
                self.sales_low_box6,
                self.sales_low_box7,
                self.earning_low_box1,
                self.earning_low_box2,
                self.earning_low_box3,
                self.earning_low_box4,
                self.earning_low_box5,
                self.earning_low_box6,
                self.earning_low_box7,
                self.sales_year_ago_box1,
                self.sales_year_ago_box2,
                self.sales_year_ago_box3,
                self.sales_year_ago_box4,
                self.sales_year_ago_box5,
                self.sales_year_ago_box6,
                self.sales_year_ago_box7,
                self.earning_year_ago_box1,
                self.earning_year_ago_box2,
                self.earning_year_ago_box3,
                self.earning_year_ago_box4,
                self.earning_year_ago_box5,
                self.earning_year_ago_box6,
                self.earning_year_ago_box7,
                self.symbol
            )
        )
        conn.commit()
        conn.close()

    def symbol_in_consensus_table(self):
        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
                    select id from consensus_analysis_data where consensus_analysis_data.symbol=?
                """
        cur.execute(sql_query, (self.symbol,))
        rows_count = len(cur.fetchall())
        conn.close()
        return rows_count == 1


class ReutersDBRevenueTable(ReutersDBConnection):
    """
    insert, update, select and delete from revenue table
    """
    def __init__(
            self,
            symbol,
            revenue_earnings_per_share_year_box1,
            revenue_earnings_per_share_year_box2,
            revenue_earnings_per_share_year_box3,
            revenue_earnings_per_share_year_box4,
            revenue_earnings_per_share_month_box1,
            revenue_earnings_per_share_month_box2,
            revenue_earnings_per_share_month_box3,
            revenue_earnings_per_share_month_box4,
            revenue_earnings_per_share_month_box5,
            revenue_earnings_per_share_month_box6,
            revenue_earnings_per_share_month_box7,
            revenue_earnings_per_share_month_box8,
            revenue_earnings_per_share_month_box9,
            revenue_earnings_per_share_month_box10,
            revenue_earnings_per_share_month_box11,
            revenue_earnings_per_share_month_box12,
            revenue_earnings_per_share_month_box13,
            revenue_box1,
            revenue_box2,
            revenue_box3,
            revenue_box4,
            revenue_box5,
            revenue_box6,
            revenue_box7,
            revenue_box8,
            revenue_box9,
            revenue_box10,
            revenue_box11,
            revenue_box12,
            revenue_box13,
            earnings_per_share_box1,
            earnings_per_share_box2,
            earnings_per_share_box3,
            earnings_per_share_box4,
            earnings_per_share_box5,
            earnings_per_share_box6,
            earnings_per_share_box7,
            earnings_per_share_box8,
            earnings_per_share_box9,
            earnings_per_share_box10,
            earnings_per_share_box11,
            earnings_per_share_box12,
            earnings_per_share_box13,
            date_scrapped
    ):
        self.symbol = symbol
        self.revenue_earnings_per_share_year_box1 = revenue_earnings_per_share_year_box1
        self.revenue_earnings_per_share_year_box2 = revenue_earnings_per_share_year_box2
        self.revenue_earnings_per_share_year_box3 = revenue_earnings_per_share_year_box3
        self.revenue_earnings_per_share_year_box4 = revenue_earnings_per_share_year_box4
        self.revenue_earnings_per_share_month_box1 = revenue_earnings_per_share_month_box1
        self.revenue_earnings_per_share_month_box2 = revenue_earnings_per_share_month_box2
        self.revenue_earnings_per_share_month_box3 = revenue_earnings_per_share_month_box3
        self.revenue_earnings_per_share_month_box4 = revenue_earnings_per_share_month_box4
        self.revenue_earnings_per_share_month_box5 = revenue_earnings_per_share_month_box5
        self.revenue_earnings_per_share_month_box6 = revenue_earnings_per_share_month_box6
        self.revenue_earnings_per_share_month_box7 = revenue_earnings_per_share_month_box7
        self.revenue_earnings_per_share_month_box8 = revenue_earnings_per_share_month_box8
        self.revenue_earnings_per_share_month_box9 = revenue_earnings_per_share_month_box9
        self.revenue_earnings_per_share_month_box10 = revenue_earnings_per_share_month_box10
        self.revenue_earnings_per_share_month_box11 = revenue_earnings_per_share_month_box11
        self.revenue_earnings_per_share_month_box12 = revenue_earnings_per_share_month_box12
        self.revenue_earnings_per_share_month_box13 = revenue_earnings_per_share_month_box13
        self.revenue_box1 = revenue_box1
        self.revenue_box2 = revenue_box2
        self.revenue_box3 = revenue_box3
        self.revenue_box4 = revenue_box4
        self.revenue_box5 = revenue_box5
        self.revenue_box6 = revenue_box6
        self.revenue_box7 = revenue_box7
        self.revenue_box8 = revenue_box8
        self.revenue_box9 = revenue_box9
        self.revenue_box10 = revenue_box10
        self.revenue_box11 = revenue_box11
        self.revenue_box12 = revenue_box12
        self.revenue_box13 = revenue_box13
        self.earnings_per_share_box1 = earnings_per_share_box1
        self.earnings_per_share_box2 = earnings_per_share_box2
        self.earnings_per_share_box3 = earnings_per_share_box3
        self.earnings_per_share_box4 = earnings_per_share_box4
        self.earnings_per_share_box5 = earnings_per_share_box5
        self.earnings_per_share_box6 = earnings_per_share_box6
        self.earnings_per_share_box7 = earnings_per_share_box7
        self.earnings_per_share_box8 = earnings_per_share_box8
        self.earnings_per_share_box9 = earnings_per_share_box9
        self.earnings_per_share_box10 = earnings_per_share_box10
        self.earnings_per_share_box11 = earnings_per_share_box11
        self.earnings_per_share_box12 = earnings_per_share_box12
        self.earnings_per_share_box13 = earnings_per_share_box13
        self.date_scrapped = date_scrapped

    def insert_record_revenue_table(self):

        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            insert into revenue_earnings_per_share (
                symbol,
                revenue_earnings_per_share_year_box1,
                revenue_earnings_per_share_year_box2,
                revenue_earnings_per_share_year_box3,
                revenue_earnings_per_share_year_box4,
                revenue_earnings_per_share_month_box1,
                revenue_earnings_per_share_month_box2,
                revenue_earnings_per_share_month_box3,
                revenue_earnings_per_share_month_box4,
                revenue_earnings_per_share_month_box5,
                revenue_earnings_per_share_month_box6,
                revenue_earnings_per_share_month_box7,
                revenue_earnings_per_share_month_box8,
                revenue_earnings_per_share_month_box9,
                revenue_earnings_per_share_month_box10,
                revenue_earnings_per_share_month_box11,
                revenue_earnings_per_share_month_box12,
                revenue_earnings_per_share_month_box13,
                revenue_box1,
                revenue_box2,
                revenue_box3,
                revenue_box4,
                revenue_box5,
                revenue_box6,
                revenue_box7,
                revenue_box8,
                revenue_box9,
                revenue_box10,
                revenue_box11,
                revenue_box12,
                revenue_box13,
                earnings_per_share_box1,
                earnings_per_share_box2,
                earnings_per_share_box3,
                earnings_per_share_box4,
                earnings_per_share_box5,
                earnings_per_share_box6,
                earnings_per_share_box7,
                earnings_per_share_box8,
                earnings_per_share_box9,
                earnings_per_share_box10,
                earnings_per_share_box11,
                earnings_per_share_box12,
                earnings_per_share_box13,
                date_scrapped
            ) values (
			?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,
			?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,
			?, ?, ?,?
		)
        """
        cur.execute(
            sql_query, (
                self.symbol,
                self.revenue_earnings_per_share_year_box1,
                self.revenue_earnings_per_share_year_box2,
                self.revenue_earnings_per_share_year_box3,
                self.revenue_earnings_per_share_year_box4,
                self.revenue_earnings_per_share_month_box1,
                self.revenue_earnings_per_share_month_box2,
                self.revenue_earnings_per_share_month_box3,
                self.revenue_earnings_per_share_month_box4,
                self.revenue_earnings_per_share_month_box5,
                self.revenue_earnings_per_share_month_box6,
                self.revenue_earnings_per_share_month_box7,
                self.revenue_earnings_per_share_month_box8,
                self.revenue_earnings_per_share_month_box9,
                self.revenue_earnings_per_share_month_box10,
                self.revenue_earnings_per_share_month_box11,
                self.revenue_earnings_per_share_month_box12,
                self.revenue_earnings_per_share_month_box13,
                self.revenue_box1,
                self.revenue_box2,
                self.revenue_box3,
                self.revenue_box4,
                self.revenue_box5,
                self.revenue_box6,
                self.revenue_box7,
                self.revenue_box8,
                self.revenue_box9,
                self.revenue_box10,
                self.revenue_box11,
                self.revenue_box12,
                self.revenue_box13,
                self.earnings_per_share_box1,
                self.earnings_per_share_box2,
                self.earnings_per_share_box3,
                self.earnings_per_share_box4,
                self.earnings_per_share_box5,
                self.earnings_per_share_box6,
                self.earnings_per_share_box7,
                self.earnings_per_share_box8,
                self.earnings_per_share_box9,
                self.earnings_per_share_box10,
                self.earnings_per_share_box11,
                self.earnings_per_share_box12,
                self.earnings_per_share_box13,
                self.date_scrapped
            )
        )
        conn.commit()
        conn.close()

    def update_record_revenue_table(self):

        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            update revenue_earnings_per_share
            set revenue_earnings_per_share_year_box1=?,
                revenue_earnings_per_share_year_box2=?,
                revenue_earnings_per_share_year_box3=?,
                revenue_earnings_per_share_year_box4=?,
                revenue_earnings_per_share_month_box1=?,
                revenue_earnings_per_share_month_box2=?,
                revenue_earnings_per_share_month_box3=?,
                revenue_earnings_per_share_month_box4=?,
                revenue_earnings_per_share_month_box5=?,
                revenue_earnings_per_share_month_box6=?,
                revenue_earnings_per_share_month_box7=?,
                revenue_earnings_per_share_month_box8=?,
                revenue_earnings_per_share_month_box9=?,
                revenue_earnings_per_share_month_box10=?,
                revenue_earnings_per_share_month_box11=?,
                revenue_earnings_per_share_month_box12=?,
                revenue_earnings_per_share_month_box13=?,
                revenue_box1=?,
                revenue_box2=?,
                revenue_box3=?,
                revenue_box4=?,
                revenue_box5=?,
                revenue_box6=?,
                revenue_box7=?,
                revenue_box8=?,
                revenue_box9=?,
                revenue_box10=?,
                revenue_box11=?,
                revenue_box12=?,
                revenue_box13=?,
                earnings_per_share_box1=?,
                earnings_per_share_box2=?,
                earnings_per_share_box3=?,
                earnings_per_share_box4=?,
                earnings_per_share_box5=?,
                earnings_per_share_box6=?,
                earnings_per_share_box7=?,
                earnings_per_share_box8=?,
                earnings_per_share_box9=?,
                earnings_per_share_box10=?,
                earnings_per_share_box11=?,
                earnings_per_share_box12=?,
                earnings_per_share_box13=?
            where symbol=?
        """
        cur.execute(
            sql_query, (
                self.revenue_earnings_per_share_year_box1,
                self.revenue_earnings_per_share_year_box2,
                self.revenue_earnings_per_share_year_box3,
                self.revenue_earnings_per_share_year_box4,
                self.revenue_earnings_per_share_month_box1,
                self.revenue_earnings_per_share_month_box2,
                self.revenue_earnings_per_share_month_box3,
                self.revenue_earnings_per_share_month_box4,
                self.revenue_earnings_per_share_month_box5,
                self.revenue_earnings_per_share_month_box6,
                self.revenue_earnings_per_share_month_box7,
                self.revenue_earnings_per_share_month_box8,
                self.revenue_earnings_per_share_month_box9,
                self.revenue_earnings_per_share_month_box10,
                self.revenue_earnings_per_share_month_box11,
                self.revenue_earnings_per_share_month_box12,
                self.revenue_earnings_per_share_month_box13,
                self.revenue_box1,
                self.revenue_box2,
                self.revenue_box3,
                self.revenue_box4,
                self.revenue_box5,
                self.revenue_box6,
                self.revenue_box7,
                self.revenue_box8,
                self.revenue_box9,
                self.revenue_box10,
                self.revenue_box11,
                self.revenue_box12,
                self.revenue_box13,
                self.earnings_per_share_box1,
                self.earnings_per_share_box2,
                self.earnings_per_share_box3,
                self.earnings_per_share_box4,
                self.earnings_per_share_box5,
                self.earnings_per_share_box6,
                self.earnings_per_share_box7,
                self.earnings_per_share_box8,
                self.earnings_per_share_box9,
                self.earnings_per_share_box10,
                self.earnings_per_share_box11,
                self.earnings_per_share_box12,
                self.earnings_per_share_box13,
                self.symbol
            )
        )
        conn.commit()
        conn.close()

    def symbol_in_revenue_table(self):
        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            select id from revenue_earnings_per_share where symbol=?
        """
        cur.execute(sql_query, (self.symbol,))
        rows_count = len(cur.fetchall())
        conn.close()
        return rows_count == 1


class ReutersDBValuationRatiosTable(ReutersDBConnection):
    """
    insert, update, select and delete from info_pages table
    """
    def __init__(
            self,
            symbol,
            valuation_ratios_name_box1,
            valuation_ratios_company_box1,
            valuation_ratios_industry_box1,
            valuation_ratios_sector_box1,
            valuation_ratios_name_box2,
            valuation_ratios_company_box2,
            valuation_ratios_industry_box2,
            valuation_ratios_sector_box2,
            valuation_ratios_name_box3,
            valuation_ratios_company_box3,
            valuation_ratios_industry_box3,
            valuation_ratios_sector_box3,
            valuation_ratios_name_box4,
            valuation_ratios_company_box4,
            valuation_ratios_industry_box4,
            valuation_ratios_sector_box4,
            valuation_ratios_name_box5,
            valuation_ratios_company_box5,
            valuation_ratios_industry_box5,
            valuation_ratios_sector_box5,
            valuation_ratios_name_box6,
            valuation_ratios_company_box6,
            valuation_ratios_industry_box6,
            valuation_ratios_sector_box6,
            valuation_ratios_name_box7,
            valuation_ratios_company_box7,
            valuation_ratios_industry_box7,
            valuation_ratios_sector_box7,
            valuation_ratios_name_box8,
            valuation_ratios_company_box8,
            valuation_ratios_industry_box8,
            valuation_ratios_sector_box8,
            valuation_ratios_name_box9,
            valuation_ratios_company_box9,
            valuation_ratios_industry_box9,
            valuation_ratios_sector_box9,
            date_scrapped
    ):
        self.symbol = symbol
        self.valuation_ratios_name_box1 = valuation_ratios_name_box1
        self.valuation_ratios_company_box1 = valuation_ratios_company_box1
        self.valuation_ratios_industry_box1 = valuation_ratios_industry_box1
        self.valuation_ratios_sector_box1 = valuation_ratios_sector_box1
        self.valuation_ratios_name_box2 = valuation_ratios_name_box2
        self.valuation_ratios_company_box2 = valuation_ratios_company_box2
        self.valuation_ratios_industry_box2 = valuation_ratios_industry_box2
        self.valuation_ratios_sector_box2 = valuation_ratios_sector_box2
        self.valuation_ratios_name_box3 = valuation_ratios_name_box3
        self.valuation_ratios_company_box3 = valuation_ratios_company_box3
        self.valuation_ratios_industry_box3 = valuation_ratios_industry_box3
        self.valuation_ratios_sector_box3 = valuation_ratios_sector_box3
        self.valuation_ratios_name_box4 = valuation_ratios_name_box4
        self.valuation_ratios_company_box4 = valuation_ratios_company_box4
        self.valuation_ratios_industry_box4 = valuation_ratios_industry_box4
        self.valuation_ratios_sector_box4 = valuation_ratios_sector_box4
        self.valuation_ratios_name_box5 = valuation_ratios_name_box5
        self.valuation_ratios_company_box5 = valuation_ratios_company_box5
        self.valuation_ratios_industry_box5 = valuation_ratios_industry_box5
        self.valuation_ratios_sector_box5 = valuation_ratios_sector_box5
        self.valuation_ratios_name_box6 = valuation_ratios_name_box6
        self.valuation_ratios_company_box6 = valuation_ratios_company_box6
        self.valuation_ratios_industry_box6 = valuation_ratios_industry_box6
        self.valuation_ratios_sector_box6 = valuation_ratios_sector_box6
        self.valuation_ratios_name_box7 = valuation_ratios_name_box7
        self.valuation_ratios_company_box7 = valuation_ratios_company_box7
        self.valuation_ratios_industry_box7 = valuation_ratios_industry_box7
        self.valuation_ratios_sector_box7 = valuation_ratios_sector_box7
        self.valuation_ratios_name_box8 = valuation_ratios_name_box8
        self.valuation_ratios_company_box8 = valuation_ratios_company_box8
        self.valuation_ratios_industry_box8 = valuation_ratios_industry_box8
        self.valuation_ratios_sector_box8 = valuation_ratios_sector_box8
        self.valuation_ratios_name_box9 = valuation_ratios_name_box9
        self.valuation_ratios_company_box9 = valuation_ratios_company_box9
        self.valuation_ratios_industry_box9 = valuation_ratios_industry_box9
        self.valuation_ratios_sector_box9 = valuation_ratios_sector_box9
        self.date_scrapped = date_scrapped


    def insert_record_valuation_ratios_table(self):

        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            insert into valuation_ratios (
                symbol,
                valuation_ratios_name_box1,
                valuation_ratios_company_box1,
                valuation_ratios_industry_box1,
                valuation_ratios_sector_box1,
                valuation_ratios_name_box2,
                valuation_ratios_company_box2,
                valuation_ratios_industry_box2,
                valuation_ratios_sector_box2,
                valuation_ratios_name_box3,
                valuation_ratios_company_box3,
                valuation_ratios_industry_box3,
                valuation_ratios_sector_box3,
                valuation_ratios_name_box4,
                valuation_ratios_company_box4,
                valuation_ratios_industry_box4,
                valuation_ratios_sector_box4,
                valuation_ratios_name_box5,
                valuation_ratios_company_box5,
                valuation_ratios_industry_box5,
                valuation_ratios_sector_box5,
                valuation_ratios_name_box6,
                valuation_ratios_company_box6,
                valuation_ratios_industry_box6,
                valuation_ratios_sector_box6,
                valuation_ratios_name_box7,
                valuation_ratios_company_box7,
                valuation_ratios_industry_box7,
                valuation_ratios_sector_box7,
                valuation_ratios_name_box8,
                valuation_ratios_company_box8,
                valuation_ratios_industry_box8,
                valuation_ratios_sector_box8,
                valuation_ratios_name_box9,
                valuation_ratios_company_box9,
                valuation_ratios_industry_box9,
                valuation_ratios_sector_box9,
                date_scrapped
            )
            values (?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?)
        """
        cur.execute(
            sql_query, (
                self.symbol,
                self.valuation_ratios_name_box1,
                self.valuation_ratios_company_box1,
                self.valuation_ratios_industry_box1,
                self.valuation_ratios_sector_box1,
                self.valuation_ratios_name_box2,
                self.valuation_ratios_company_box2,
                self.valuation_ratios_industry_box2,
                self.valuation_ratios_sector_box2,
                self.valuation_ratios_name_box3,
                self.valuation_ratios_company_box3,
                self.valuation_ratios_industry_box3,
                self.valuation_ratios_sector_box3,
                self.valuation_ratios_name_box4,
                self.valuation_ratios_company_box4,
                self.valuation_ratios_industry_box4,
                self.valuation_ratios_sector_box4,
                self.valuation_ratios_name_box5,
                self.valuation_ratios_company_box5,
                self.valuation_ratios_industry_box5,
                self.valuation_ratios_sector_box5,
                self.valuation_ratios_name_box6,
                self.valuation_ratios_company_box6,
                self.valuation_ratios_industry_box6,
                self.valuation_ratios_sector_box6,
                self.valuation_ratios_name_box7,
                self.valuation_ratios_company_box7,
                self.valuation_ratios_industry_box7,
                self.valuation_ratios_sector_box7,
                self.valuation_ratios_name_box8,
                self.valuation_ratios_company_box8,
                self.valuation_ratios_industry_box8,
                self.valuation_ratios_sector_box8,
                self.valuation_ratios_name_box9,
                self.valuation_ratios_company_box9,
                self.valuation_ratios_industry_box9,
                self.valuation_ratios_sector_box9,
                self.date_scrapped
            )
        )
        conn.commit()
        conn.close()

    def update_record_valuation_ratios_table(self):

        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            update valuation_ratios
            set valuation_ratios_name_box1=?,
                valuation_ratios_company_box1=?,
                valuation_ratios_industry_box1=?,
                valuation_ratios_sector_box1=?,
                valuation_ratios_name_box2=?,
                valuation_ratios_company_box2=?,
                valuation_ratios_industry_box2=?,
                valuation_ratios_sector_box2=?,
                valuation_ratios_name_box3=?,
                valuation_ratios_company_box3=?,
                valuation_ratios_industry_box3=?,
                valuation_ratios_sector_box3=?,
                valuation_ratios_name_box4=?,
                valuation_ratios_company_box4=?,
                valuation_ratios_industry_box4=?,
                valuation_ratios_sector_box4=?,
                valuation_ratios_name_box5=?,
                valuation_ratios_company_box5=?,
                valuation_ratios_industry_box5=?,
                valuation_ratios_sector_box5=?,
                valuation_ratios_name_box6=?,
                valuation_ratios_company_box6=?,
                valuation_ratios_industry_box6=?,
                valuation_ratios_sector_box6=?,
                valuation_ratios_name_box7=?,
                valuation_ratios_company_box7=?,
                valuation_ratios_industry_box7=?,
                valuation_ratios_sector_box7=?,
                valuation_ratios_name_box8=?,
                valuation_ratios_company_box8=?,
                valuation_ratios_industry_box8=?,
                valuation_ratios_sector_box8=?,
                valuation_ratios_name_box9=?,
                valuation_ratios_company_box9=?,
                valuation_ratios_industry_box9=?,
                valuation_ratios_sector_box9=?
            where symbol=?
        """
        cur.execute(
            sql_query, (
                self.valuation_ratios_name_box1,
                self.valuation_ratios_company_box1,
                self.valuation_ratios_industry_box1,
                self.valuation_ratios_sector_box1,
                self.valuation_ratios_name_box2,
                self.valuation_ratios_company_box2,
                self.valuation_ratios_industry_box2,
                self.valuation_ratios_sector_box2,
                self.valuation_ratios_name_box3,
                self.valuation_ratios_company_box3,
                self.valuation_ratios_industry_box3,
                self.valuation_ratios_sector_box3,
                self.valuation_ratios_name_box4,
                self.valuation_ratios_company_box4,
                self.valuation_ratios_industry_box4,
                self.valuation_ratios_sector_box4,
                self.valuation_ratios_name_box5,
                self.valuation_ratios_company_box5,
                self.valuation_ratios_industry_box5,
                self.valuation_ratios_sector_box5,
                self.valuation_ratios_name_box6,
                self.valuation_ratios_company_box6,
                self.valuation_ratios_industry_box6,
                self.valuation_ratios_sector_box6,
                self.valuation_ratios_name_box7,
                self.valuation_ratios_company_box7,
                self.valuation_ratios_industry_box7,
                self.valuation_ratios_sector_box7,
                self.valuation_ratios_name_box8,
                self.valuation_ratios_company_box8,
                self.valuation_ratios_industry_box8,
                self.valuation_ratios_sector_box8,
                self.valuation_ratios_name_box9,
                self.valuation_ratios_company_box9,
                self.valuation_ratios_industry_box9,
                self.valuation_ratios_sector_box9,
                self.symbol
            )
        )
        conn.commit()
        conn.close()

    def symbol_in_valuation_ratios_table(self):
        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            select id from valuation_ratios where symbol=?
        """
        cur.execute(sql_query, (self.symbol,))
        rows_count = len(cur.fetchall())
        conn.close()
        return rows_count == 1


class ReutersDBDividendsTable(ReutersDBConnection):
    """
    insert, update, select and delete from dividends table
    """
    def __init__(
            self,
            symbol,
            dividends_name_box1,
            dividends_company_box1,
            dividends_industry_box1,
            dividends_sector_box1,
            dividends_name_box2,
            dividends_company_box2,
            dividends_industry_box2,
            dividends_sector_box2,
            dividends_name_box3,
            dividends_company_box3,
            dividends_industry_box3,
            dividends_sector_box3,
            dividends_name_box4,
            dividends_company_box4,
            dividends_industry_box4,
            dividends_sector_box4,
            date_scrapped
    ):
        self.symbol = symbol
        self.dividends_name_box1 = dividends_name_box1
        self.dividends_company_box1 = dividends_company_box1
        self.dividends_industry_box1 = dividends_industry_box1
        self.dividends_sector_box1 = dividends_sector_box1
        self.dividends_name_box2 = dividends_name_box2
        self.dividends_company_box2 = dividends_company_box2
        self.dividends_industry_box2 = dividends_industry_box2
        self.dividends_sector_box2 = dividends_sector_box2
        self.dividends_name_box3 = dividends_name_box3
        self.dividends_company_box3 = dividends_company_box3
        self.dividends_industry_box3 = dividends_industry_box3
        self.dividends_sector_box3 = dividends_sector_box3
        self.dividends_name_box4 = dividends_name_box4
        self.dividends_company_box4 = dividends_company_box4
        self.dividends_industry_box4 = dividends_industry_box4
        self.dividends_sector_box4 = dividends_sector_box4
        self.date_scrapped = date_scrapped

    def insert_record_dividends_table(self):

        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            insert into dividends (
                symbol,
                dividends_name_box1,
                dividends_company_box1,
                dividends_industry_box1,
                dividends_sector_box1,
                dividends_name_box2,
                dividends_company_box2,
                dividends_industry_box2,
                dividends_sector_box2,
                dividends_name_box3,
                dividends_company_box3,
                dividends_industry_box3,
                dividends_sector_box3,
                dividends_name_box4,
                dividends_company_box4,
                dividends_industry_box4,
                dividends_sector_box4,
                date_scrapped
            )
            values (?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?)
        """
        cur.execute(
            sql_query, (
                self.symbol,
                self.dividends_name_box1,
                self.dividends_company_box1,
                self.dividends_industry_box1,
                self.dividends_sector_box1,
                self.dividends_name_box2,
                self.dividends_company_box2,
                self.dividends_industry_box2,
                self.dividends_sector_box2,
                self.dividends_name_box3,
                self.dividends_company_box3,
                self.dividends_industry_box3,
                self.dividends_sector_box3,
                self.dividends_name_box4,
                self.dividends_company_box4,
                self.dividends_industry_box4,
                self.dividends_sector_box4,
                self.date_scrapped
            )
        )
        conn.commit()
        conn.close()

    def update_record_dividends_table(self):

        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            update dividends
            set dividends_name_box1=?,
                dividends_company_box1=?,
                dividends_industry_box1=?,
                dividends_sector_box1=?,
                dividends_name_box2=?,
                dividends_company_box2=?,
                dividends_industry_box2=?,
                dividends_sector_box2=?,
                dividends_name_box3=?,
                dividends_company_box3=?,
                dividends_industry_box3=?,
                dividends_sector_box3=?,
                dividends_name_box4=?,
                dividends_company_box4=?,
                dividends_industry_box4=?,
                dividends_sector_box4=?
            where symbol=?
        """
        cur.execute(
            sql_query, (
                self.dividends_name_box1,
                self.dividends_company_box1,
                self.dividends_industry_box1,
                self.dividends_sector_box1,
                self.dividends_name_box2,
                self.dividends_company_box2,
                self.dividends_industry_box2,
                self.dividends_sector_box2,
                self.dividends_name_box3,
                self.dividends_company_box3,
                self.dividends_industry_box3,
                self.dividends_sector_box3,
                self.dividends_name_box4,
                self.dividends_company_box4,
                self.dividends_industry_box4,
                self.dividends_sector_box4,
                self.symbol
            )
        )
        conn.commit()
        conn.close()

    def symbol_in_dividends_table(self):
        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            select id from dividends where symbol=?
        """
        cur.execute(sql_query, (self.symbol,))
        rows_count = len(cur.fetchall())
        conn.close()
        return rows_count == 1


class ReutersDBGrowthRatesTable(ReutersDBConnection):
    """
    insert, update, select and delete from growth_rates table
    """
    def __init__(
            self,
            symbol,
            growth_rates_name_box1,
            growth_rates_name_box2,

            growth_rates_name_box3,
            growth_rates_name_box4,
            growth_rates_name_box5,
            growth_rates_name_box6,
            growth_rates_name_box7,

            growth_rates_company_box1,
            growth_rates_company_box2,
            growth_rates_company_box3,
            growth_rates_company_box4,
            growth_rates_company_box5,
            growth_rates_company_box6,
            growth_rates_company_box7,

            growth_rates_industry_box1,
            growth_rates_industry_box2,
            growth_rates_industry_box3,
            growth_rates_industry_box4,
            growth_rates_industry_box5,
            growth_rates_industry_box6,
            growth_rates_industry_box7,

            growth_rates_sector_box1,
            growth_rates_sector_box2,
            growth_rates_sector_box3,
            growth_rates_sector_box4,
            growth_rates_sector_box5,
            growth_rates_sector_box6,
            growth_rates_sector_box7,
            date_scrapped
    ):
        self.symbol = symbol
        self.growth_rates_name_box1 = growth_rates_name_box1
        self.growth_rates_name_box2 = growth_rates_name_box2
        self.growth_rates_name_box3 = growth_rates_name_box3
        self.growth_rates_name_box4 = growth_rates_name_box4
        self.growth_rates_name_box5 = growth_rates_name_box5
        self.growth_rates_name_box6 = growth_rates_name_box6
        self.growth_rates_name_box7 = growth_rates_name_box7
        self.growth_rates_company_box1 = growth_rates_company_box1
        self.growth_rates_company_box2 = growth_rates_company_box2
        self.growth_rates_company_box3 = growth_rates_company_box3
        self.growth_rates_company_box4 = growth_rates_company_box4
        self.growth_rates_company_box5 = growth_rates_company_box5
        self.growth_rates_company_box6 = growth_rates_company_box6
        self.growth_rates_company_box7 = growth_rates_company_box7
        self.growth_rates_industry_box1 = growth_rates_industry_box1
        self.growth_rates_industry_box2 = growth_rates_industry_box2
        self.growth_rates_industry_box3 = growth_rates_industry_box3
        self.growth_rates_industry_box4 = growth_rates_industry_box4
        self.growth_rates_industry_box5 = growth_rates_industry_box5
        self.growth_rates_industry_box6 = growth_rates_industry_box6
        self.growth_rates_industry_box7 = growth_rates_industry_box7
        self.growth_rates_sector_box1 = growth_rates_sector_box1
        self.growth_rates_sector_box2 = growth_rates_sector_box2
        self.growth_rates_sector_box3 = growth_rates_sector_box3
        self.growth_rates_sector_box4 = growth_rates_sector_box4
        self.growth_rates_sector_box5 = growth_rates_sector_box5
        self.growth_rates_sector_box6 = growth_rates_sector_box6
        self.growth_rates_sector_box7 = growth_rates_sector_box7
        self.date_scrapped = date_scrapped

    def insert_record_growth_rates_table(self):

        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            insert into growth_rates (
                symbol,
                growth_rates_name_box1,
                growth_rates_name_box2,

                growth_rates_name_box3,
                growth_rates_name_box4,
                growth_rates_name_box5,
                growth_rates_name_box6,
                growth_rates_name_box7,

                growth_rates_company_box1,
                growth_rates_company_box2,
                growth_rates_company_box3,
                growth_rates_company_box4,
                growth_rates_company_box5,
                growth_rates_company_box6,
                growth_rates_company_box7,

                growth_rates_industry_box1,
                growth_rates_industry_box2,
                growth_rates_industry_box3,
                growth_rates_industry_box4,
                growth_rates_industry_box5,
                growth_rates_industry_box6,
                growth_rates_industry_box7,

                growth_rates_sector_box1,
                growth_rates_sector_box2,
                growth_rates_sector_box3,
                growth_rates_sector_box4,
                growth_rates_sector_box5,
                growth_rates_sector_box6,
                growth_rates_sector_box7,
                date_scrapped
            )
            values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cur.execute(
            sql_query, (
                self.symbol,
                self.growth_rates_name_box1,
                self.growth_rates_name_box2,
                self.growth_rates_name_box3,
                self.growth_rates_name_box4,
                self.growth_rates_name_box5,
                self.growth_rates_name_box6,
                self.growth_rates_name_box7,
                self.growth_rates_company_box1,
                self.growth_rates_company_box2,
                self.growth_rates_company_box3,
                self.growth_rates_company_box4,
                self.growth_rates_company_box5,
                self.growth_rates_company_box6,
                self.growth_rates_company_box7,
                self.growth_rates_industry_box1,
                self.growth_rates_industry_box2,
                self.growth_rates_industry_box3,
                self.growth_rates_industry_box4,
                self.growth_rates_industry_box5,
                self.growth_rates_industry_box6,
                self.growth_rates_industry_box7,
                self.growth_rates_sector_box1,
                self.growth_rates_sector_box2,
                self.growth_rates_sector_box3,
                self.growth_rates_sector_box4,
                self.growth_rates_sector_box5,
                self.growth_rates_sector_box6,
                self.growth_rates_sector_box7,
                self.date_scrapped
            )
        )
        conn.commit()
        conn.close()

    def update_record_growth_rates_table(self):

        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            update growth_rates
            set growth_rates_name_box1=?,
                growth_rates_name_box2=?,
                growth_rates_name_box3=?,
                growth_rates_name_box4=?,
                growth_rates_name_box5=?,
                growth_rates_name_box6=?,
                growth_rates_name_box7=?,
                growth_rates_company_box1=?,
                growth_rates_company_box2=?,
                growth_rates_company_box3=?,
                growth_rates_company_box4=?,
                growth_rates_company_box5=?,
                growth_rates_company_box6=?,
                growth_rates_company_box7=?,
                growth_rates_industry_box1=?,
                growth_rates_industry_box2=?,
                growth_rates_industry_box3=?,
                growth_rates_industry_box4=?,
                growth_rates_industry_box5=?,
                growth_rates_industry_box6=?,
                growth_rates_industry_box7=?,
                growth_rates_sector_box1=?,
                growth_rates_sector_box2=?,
                growth_rates_sector_box3=?,
                growth_rates_sector_box4=?,
                growth_rates_sector_box5=?,
                growth_rates_sector_box6=?,
                growth_rates_sector_box7=?
            where symbol=?
        """
        cur.execute(
            sql_query, (
                self.growth_rates_name_box1,
                self.growth_rates_name_box2,
                self.growth_rates_name_box3,
                self.growth_rates_name_box4,
                self.growth_rates_name_box5,
                self.growth_rates_name_box6,
                self.growth_rates_name_box7,
                self.growth_rates_company_box1,
                self.growth_rates_company_box2,
                self.growth_rates_company_box3,
                self.growth_rates_company_box4,
                self.growth_rates_company_box5,
                self.growth_rates_company_box6,
                self.growth_rates_company_box7,
                self.growth_rates_industry_box1,
                self.growth_rates_industry_box2,
                self.growth_rates_industry_box3,
                self.growth_rates_industry_box4,
                self.growth_rates_industry_box5,
                self.growth_rates_industry_box6,
                self.growth_rates_industry_box7,
                self.growth_rates_sector_box1,
                self.growth_rates_sector_box2,
                self.growth_rates_sector_box3,
                self.growth_rates_sector_box4,
                self.growth_rates_sector_box5,
                self.growth_rates_sector_box6,
                self.growth_rates_sector_box7,
                self.symbol
            )
        )
        conn.commit()
        conn.close()

    def symbol_in_growth_rates_table(self):
        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            select id from growth_rates where symbol=?
        """
        cur.execute(sql_query, (self.symbol,))
        rows_count = len(cur.fetchall())
        conn.close()
        return rows_count == 1


class ReutersDBFinancialStrengthTable(ReutersDBConnection):
    """
    insert, update, select and delete from financial_strength table
    """
    def __init__(
            self,
            symbol,
            financial_strength_name_box1,
            financial_strength_company_box1,

            financial_strength_industry_box1,
            financial_strength_sector_box1,

            financial_strength_name_box2,
            financial_strength_company_box2,
            financial_strength_industry_box2,
            financial_strength_sector_box2,

            financial_strength_name_box3,
            financial_strength_company_box3,
            financial_strength_industry_box3,
            financial_strength_sector_box3,

            financial_strength_name_box4,
            financial_strength_company_box4,
            financial_strength_industry_box4,
            financial_strength_sector_box4,

            financial_strength_name_box5,
            financial_strength_company_box5,
            financial_strength_industry_box5,
            financial_strength_sector_box5,
            date_scrapped
    ):
        self.symbol = symbol
        self.financial_strength_name_box1 = financial_strength_name_box1
        self.financial_strength_company_box1 = financial_strength_company_box1
        self.financial_strength_industry_box1 = financial_strength_industry_box1
        self.financial_strength_sector_box1 = financial_strength_sector_box1
        self.financial_strength_name_box2 = financial_strength_name_box2
        self.financial_strength_company_box2 = financial_strength_company_box2
        self.financial_strength_industry_box2 = financial_strength_industry_box2
        self.financial_strength_sector_box2 = financial_strength_sector_box2
        self.financial_strength_name_box3 = financial_strength_name_box3
        self.financial_strength_company_box3 = financial_strength_company_box3
        self.financial_strength_industry_box3 = financial_strength_industry_box3
        self.financial_strength_sector_box3 = financial_strength_sector_box3
        self.financial_strength_name_box4 = financial_strength_name_box4
        self.financial_strength_company_box4 = financial_strength_company_box4
        self.financial_strength_industry_box4 = financial_strength_industry_box4
        self.financial_strength_sector_box4 = financial_strength_sector_box4
        self.financial_strength_name_box5 = financial_strength_name_box5
        self.financial_strength_company_box5 = financial_strength_company_box5
        self.financial_strength_industry_box5 = financial_strength_industry_box5
        self.financial_strength_sector_box5 = financial_strength_sector_box5
        self.date_scrapped = date_scrapped

    def insert_record_financial_strength_table(self):

        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            insert into financial_strength (
                symbol,
                financial_strength_name_box1,
                financial_strength_company_box1,
                financial_strength_industry_box1,
                financial_strength_sector_box1,

                financial_strength_name_box2,
                financial_strength_company_box2,
                financial_strength_industry_box2,
                financial_strength_sector_box2,

                financial_strength_name_box3,
                financial_strength_company_box3,
                financial_strength_industry_box3,
                financial_strength_sector_box3,

                financial_strength_name_box4,
                financial_strength_company_box4,
                financial_strength_industry_box4,
                financial_strength_sector_box4,

                financial_strength_name_box5,
                financial_strength_company_box5,
                financial_strength_industry_box5,
                financial_strength_sector_box5,
                date_scrapped
            )
            values (?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?,?,?,?, ?)
        """
        cur.execute(
            sql_query, (
                self.symbol,
                self.financial_strength_name_box1,
                self.financial_strength_company_box1,
                self.financial_strength_industry_box1,
                self.financial_strength_sector_box1,
                self.financial_strength_name_box2,
                self.financial_strength_company_box2,
                self.financial_strength_industry_box2,
                self.financial_strength_sector_box2,
                self.financial_strength_name_box3,
                self.financial_strength_company_box3,
                self.financial_strength_industry_box3,
                self.financial_strength_sector_box3,
                self.financial_strength_name_box4,
                self.financial_strength_company_box4,
                self.financial_strength_industry_box4,
                self.financial_strength_sector_box4,
                self.financial_strength_name_box5,
                self.financial_strength_company_box5,
                self.financial_strength_industry_box5,
                self.financial_strength_sector_box5,
                self.date_scrapped
            )
        )
        conn.commit()
        conn.close()

    def update_record_financial_strength_table(self):

        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            update financial_strength
            set financial_strength_name_box1=?,
                financial_strength_company_box1=?,
                financial_strength_industry_box1=?,
                financial_strength_sector_box1=?,

                financial_strength_name_box2=?,
                financial_strength_company_box2=?,
                financial_strength_industry_box2=?,
                financial_strength_sector_box2=?,

                financial_strength_name_box3=?,
                financial_strength_company_box3=?,
                financial_strength_industry_box3=?,
                financial_strength_sector_box3=?,

                financial_strength_name_box4=?,
                financial_strength_company_box4=?,
                financial_strength_industry_box4=?,
                financial_strength_sector_box4=?,

                financial_strength_name_box5=?,
                financial_strength_company_box5=?,
                financial_strength_industry_box5=?,
                financial_strength_sector_box5=?
            where symbol=?
        """
        cur.execute(
            sql_query, (
                self.financial_strength_name_box1,
                self.financial_strength_company_box1,
                self.financial_strength_industry_box1,
                self.financial_strength_sector_box1,
                self.financial_strength_name_box2,
                self.financial_strength_company_box2,
                self.financial_strength_industry_box2,
                self.financial_strength_sector_box2,
                self.financial_strength_name_box3,
                self.financial_strength_company_box3,
                self.financial_strength_industry_box3,
                self.financial_strength_sector_box3,
                self.financial_strength_name_box4,
                self.financial_strength_company_box4,
                self.financial_strength_industry_box4,
                self.financial_strength_sector_box4,
                self.financial_strength_name_box5,
                self.financial_strength_company_box5,
                self.financial_strength_industry_box5,
                self.financial_strength_sector_box5,
                self.symbol
            )
        )
        conn.commit()
        conn.close()

    def symbol_in_financial_strength_table(self):
        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            select id from financial_strength where symbol=?
        """
        cur.execute(sql_query, (self.symbol,))
        rows_count = len(cur.fetchall())
        conn.close()
        return rows_count == 1


class ReutersDBProfitabilityRatiosTable(ReutersDBConnection):
    """
    insert, update, select and delete from profitability_ratios table
    """
    def __init__(
            self,
            symbol,
            profitability_ratios_name_box1,
            profitability_ratios_company_box1,

            profitability_ratios_industry_box1,
            profitability_ratios_sector_box1,

            profitability_ratios_name_box2,
            profitability_ratios_company_box2,
            profitability_ratios_industry_box2,
            profitability_ratios_sector_box2,

            profitability_ratios_name_box3,
            profitability_ratios_company_box3,
            profitability_ratios_industry_box3,
            profitability_ratios_sector_box3,

            profitability_ratios_name_box4,
            profitability_ratios_company_box4,
            profitability_ratios_industry_box4,
            profitability_ratios_sector_box4,

            profitability_ratios_name_box5,
            profitability_ratios_company_box5,
            profitability_ratios_industry_box5,
            profitability_ratios_sector_box5,

            profitability_ratios_name_box6,
            profitability_ratios_company_box6,
            profitability_ratios_industry_box6,
            profitability_ratios_sector_box6,

            profitability_ratios_name_box7,
            profitability_ratios_company_box7,
            profitability_ratios_industry_box7,
            profitability_ratios_sector_box7,

            profitability_ratios_name_box8,
            profitability_ratios_company_box8,
            profitability_ratios_industry_box8,
            profitability_ratios_sector_box8,

            profitability_ratios_name_box9,
            profitability_ratios_company_box9,
            profitability_ratios_industry_box9,
            profitability_ratios_sector_box9,

            profitability_ratios_name_box10,
            profitability_ratios_company_box10,
            profitability_ratios_industry_box10,
            profitability_ratios_sector_box10,

            profitability_ratios_name_box11,
            profitability_ratios_company_box11,
            profitability_ratios_industry_box11,
            profitability_ratios_sector_box11,

            profitability_ratios_name_box12,
            profitability_ratios_company_box12,
            profitability_ratios_industry_box12,
            profitability_ratios_sector_box12,
            date_scrapped
    ):
        self.symbol = symbol
        self.profitability_ratios_name_box1 = profitability_ratios_name_box1
        self.profitability_ratios_company_box1 = profitability_ratios_company_box1
        self.profitability_ratios_industry_box1 = profitability_ratios_industry_box1
        self.profitability_ratios_sector_box1 = profitability_ratios_sector_box1
        self.profitability_ratios_name_box2 = profitability_ratios_name_box2
        self.profitability_ratios_company_box2 = profitability_ratios_company_box2
        self.profitability_ratios_industry_box2 = profitability_ratios_industry_box2
        self.profitability_ratios_sector_box2 = profitability_ratios_sector_box2
        self.profitability_ratios_name_box3 = profitability_ratios_name_box3
        self.profitability_ratios_company_box3 = profitability_ratios_company_box3
        self.profitability_ratios_industry_box3 = profitability_ratios_industry_box3
        self.profitability_ratios_sector_box3 = profitability_ratios_sector_box3
        self.profitability_ratios_name_box4 = profitability_ratios_name_box4
        self.profitability_ratios_company_box4 = profitability_ratios_company_box4
        self.profitability_ratios_industry_box4 = profitability_ratios_industry_box4
        self.profitability_ratios_sector_box4 = profitability_ratios_sector_box4
        self.profitability_ratios_name_box5 = profitability_ratios_name_box5
        self.profitability_ratios_company_box5 = profitability_ratios_company_box5
        self.profitability_ratios_industry_box5 = profitability_ratios_industry_box5
        self.profitability_ratios_sector_box5 = profitability_ratios_sector_box5
        self.profitability_ratios_name_box6 = profitability_ratios_name_box6
        self.profitability_ratios_company_box6 = profitability_ratios_company_box6
        self.profitability_ratios_industry_box6 = profitability_ratios_industry_box6
        self.profitability_ratios_sector_box6 = profitability_ratios_sector_box6
        self.profitability_ratios_name_box7 = profitability_ratios_name_box7
        self.profitability_ratios_company_box7 = profitability_ratios_company_box7
        self.profitability_ratios_industry_box7 = profitability_ratios_industry_box7
        self.profitability_ratios_sector_box7 = profitability_ratios_sector_box7
        self.profitability_ratios_name_box8 = profitability_ratios_name_box8
        self.profitability_ratios_company_box8 = profitability_ratios_company_box8
        self.profitability_ratios_industry_box8 = profitability_ratios_industry_box8
        self.profitability_ratios_sector_box8 = profitability_ratios_sector_box8
        self.profitability_ratios_name_box9 = profitability_ratios_name_box9
        self.profitability_ratios_company_box9 = profitability_ratios_company_box9
        self.profitability_ratios_industry_box9 = profitability_ratios_industry_box9
        self.profitability_ratios_sector_box9 = profitability_ratios_sector_box9
        self.profitability_ratios_name_box10 = profitability_ratios_name_box10
        self.profitability_ratios_company_box10 = profitability_ratios_company_box10
        self.profitability_ratios_industry_box10 = profitability_ratios_industry_box10
        self.profitability_ratios_sector_box10 = profitability_ratios_sector_box10
        self.profitability_ratios_name_box11 = profitability_ratios_name_box11
        self.profitability_ratios_company_box11 = profitability_ratios_company_box11
        self.profitability_ratios_industry_box11 = profitability_ratios_industry_box11
        self.profitability_ratios_sector_box11 = profitability_ratios_sector_box11
        self.profitability_ratios_name_box12 = profitability_ratios_name_box12
        self.profitability_ratios_company_box12 = profitability_ratios_company_box12
        self.profitability_ratios_industry_box12 = profitability_ratios_industry_box12
        self.profitability_ratios_sector_box12 = profitability_ratios_sector_box12
        self.date_scrapped = date_scrapped

    def insert_record_profitability_ratios_table(self):

        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            insert into profitability_ratios (
                symbol,
                profitability_ratios_name_box1,
                profitability_ratios_company_box1,

                profitability_ratios_industry_box1,
                profitability_ratios_sector_box1,

                profitability_ratios_name_box2,
                profitability_ratios_company_box2,
                profitability_ratios_industry_box2,
                profitability_ratios_sector_box2,

                profitability_ratios_name_box3,
                profitability_ratios_company_box3,
                profitability_ratios_industry_box3,
                profitability_ratios_sector_box3,

                profitability_ratios_name_box4,
                profitability_ratios_company_box4,
                profitability_ratios_industry_box4,
                profitability_ratios_sector_box4,

                profitability_ratios_name_box5,
                profitability_ratios_company_box5,
                profitability_ratios_industry_box5,
                profitability_ratios_sector_box5,

                profitability_ratios_name_box6,
                profitability_ratios_company_box6,
                profitability_ratios_industry_box6,
                profitability_ratios_sector_box6,

                profitability_ratios_name_box7,
                profitability_ratios_company_box7,
                profitability_ratios_industry_box7,
                profitability_ratios_sector_box7,

                profitability_ratios_name_box8,
                profitability_ratios_company_box8,
                profitability_ratios_industry_box8,
                profitability_ratios_sector_box8,

                profitability_ratios_name_box9,
                profitability_ratios_company_box9,
                profitability_ratios_industry_box9,
                profitability_ratios_sector_box9,

                profitability_ratios_name_box10,
                profitability_ratios_company_box10,
                profitability_ratios_industry_box10,
                profitability_ratios_sector_box10,

                profitability_ratios_name_box11,
                profitability_ratios_company_box11,
                profitability_ratios_industry_box11,
                profitability_ratios_sector_box11,

                profitability_ratios_name_box12,
                profitability_ratios_company_box12,
                profitability_ratios_industry_box12,
                profitability_ratios_sector_box12,
                date_scrapped
            )
            values (?, ?, ?, ?, ?, ?,?,?,?,?,?, ?, ?, ?, ?, ?,?,?,?,?,?, ?, ?, ?, ?, ?,?,?,?,?,
            ?, ?, ?, ?, ?, ?,?,?,?,?,?, ?, ?, ?, ?, ?,?,?,?,?)
        """
        cur.execute(
            sql_query, (
                self.symbol,
                self.profitability_ratios_name_box1,
                self.profitability_ratios_company_box1,
                self.profitability_ratios_industry_box1,
                self.profitability_ratios_sector_box1,
                self.profitability_ratios_name_box2,
                self.profitability_ratios_company_box2,
                self.profitability_ratios_industry_box2,
                self.profitability_ratios_sector_box2,
                self.profitability_ratios_name_box3,
                self.profitability_ratios_company_box3,
                self.profitability_ratios_industry_box3,
                self.profitability_ratios_sector_box3,
                self.profitability_ratios_name_box4,
                self.profitability_ratios_company_box4,
                self.profitability_ratios_industry_box4,
                self.profitability_ratios_sector_box4,
                self.profitability_ratios_name_box5,
                self.profitability_ratios_company_box5,
                self.profitability_ratios_industry_box5,
                self.profitability_ratios_sector_box5,
                self.profitability_ratios_name_box6,
                self.profitability_ratios_company_box6,
                self.profitability_ratios_industry_box6,
                self.profitability_ratios_sector_box6,
                self.profitability_ratios_name_box7,
                self.profitability_ratios_company_box7,
                self.profitability_ratios_industry_box7,
                self.profitability_ratios_sector_box7,
                self.profitability_ratios_name_box8,
                self.profitability_ratios_company_box8,
                self.profitability_ratios_industry_box8,
                self.profitability_ratios_sector_box8,
                self.profitability_ratios_name_box9,
                self.profitability_ratios_company_box9,
                self.profitability_ratios_industry_box9,
                self.profitability_ratios_sector_box9,
                self.profitability_ratios_name_box10,
                self.profitability_ratios_company_box10,
                self.profitability_ratios_industry_box10,
                self.profitability_ratios_sector_box10,
                self.profitability_ratios_name_box11,
                self.profitability_ratios_company_box11,
                self.profitability_ratios_industry_box11,
                self.profitability_ratios_sector_box11,
                self.profitability_ratios_name_box12,
                self.profitability_ratios_company_box12,
                self.profitability_ratios_industry_box12,
                self.profitability_ratios_sector_box12,
                self.date_scrapped
            )
        )
        conn.commit()
        conn.close()

    def update_record_profitability_ratios_table(self):

        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            update profitability_ratios
            set profitability_ratios_name_box1=?,
                profitability_ratios_company_box1=?,

                profitability_ratios_industry_box1=?,
                profitability_ratios_sector_box1=?,

                profitability_ratios_name_box2=?,
                profitability_ratios_company_box2=?,
                profitability_ratios_industry_box2=?,
                profitability_ratios_sector_box2=?,

                profitability_ratios_name_box3=?,
                profitability_ratios_company_box3=?,
                profitability_ratios_industry_box3=?,
                profitability_ratios_sector_box3=?,

                profitability_ratios_name_box4=?,
                profitability_ratios_company_box4=?,
                profitability_ratios_industry_box4=?,
                profitability_ratios_sector_box4=?,

                profitability_ratios_name_box5=?,
                profitability_ratios_company_box5=?,
                profitability_ratios_industry_box5=?,
                profitability_ratios_sector_box5=?,

                profitability_ratios_name_box6=?,
                profitability_ratios_company_box6=?,
                profitability_ratios_industry_box6=?,
                profitability_ratios_sector_box6=?,

                profitability_ratios_name_box7=?,
                profitability_ratios_company_box7=?,
                profitability_ratios_industry_box7=?,
                profitability_ratios_sector_box7=?,

                profitability_ratios_name_box8=?,
                profitability_ratios_company_box8=?,
                profitability_ratios_industry_box8=?,
                profitability_ratios_sector_box8=?,

                profitability_ratios_name_box9=?,
                profitability_ratios_company_box9=?,
                profitability_ratios_industry_box9=?,
                profitability_ratios_sector_box9=?,

                profitability_ratios_name_box10=?,
                profitability_ratios_company_box10=?,
                profitability_ratios_industry_box10=?,
                profitability_ratios_sector_box10=?,

                profitability_ratios_name_box11=?,
                profitability_ratios_company_box11=?,
                profitability_ratios_industry_box11=?,
                profitability_ratios_sector_box11=?,

                profitability_ratios_name_box12=?,
                profitability_ratios_company_box12=?,
                profitability_ratios_industry_box12=?,
                profitability_ratios_sector_box12=?
            where symbol=?
        """
        cur.execute(
            sql_query, (
                self.profitability_ratios_name_box1,
                self.profitability_ratios_company_box1,
                self.profitability_ratios_industry_box1,
                self.profitability_ratios_sector_box1,
                self.profitability_ratios_name_box2,
                self.profitability_ratios_company_box2,
                self.profitability_ratios_industry_box2,
                self.profitability_ratios_sector_box2,
                self.profitability_ratios_name_box3,
                self.profitability_ratios_company_box3,
                self.profitability_ratios_industry_box3,
                self.profitability_ratios_sector_box3,
                self.profitability_ratios_name_box4,
                self.profitability_ratios_company_box4,
                self.profitability_ratios_industry_box4,
                self.profitability_ratios_sector_box4,
                self.profitability_ratios_name_box5,
                self.profitability_ratios_company_box5,
                self.profitability_ratios_industry_box5,
                self.profitability_ratios_sector_box5,
                self.profitability_ratios_name_box6,
                self.profitability_ratios_company_box6,
                self.profitability_ratios_industry_box6,
                self.profitability_ratios_sector_box6,
                self.profitability_ratios_name_box7,
                self.profitability_ratios_company_box7,
                self.profitability_ratios_industry_box7,
                self.profitability_ratios_sector_box7,
                self.profitability_ratios_name_box8,
                self.profitability_ratios_company_box8,
                self.profitability_ratios_industry_box8,
                self.profitability_ratios_sector_box8,
                self.profitability_ratios_name_box9,
                self.profitability_ratios_company_box9,
                self.profitability_ratios_industry_box9,
                self.profitability_ratios_sector_box9,
                self.profitability_ratios_name_box10,
                self.profitability_ratios_company_box10,
                self.profitability_ratios_industry_box10,
                self.profitability_ratios_sector_box10,
                self.profitability_ratios_name_box11,
                self.profitability_ratios_company_box11,
                self.profitability_ratios_industry_box11,
                self.profitability_ratios_sector_box11,
                self.profitability_ratios_name_box12,
                self.profitability_ratios_company_box12,
                self.profitability_ratios_industry_box12,
                self.profitability_ratios_sector_box12,
                self.symbol
            )
        )
        conn.commit()
        conn.close()

    def symbol_in_profitability_ratios_table(self):
        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            select id from profitability_ratios where symbol=?
        """
        cur.execute(sql_query, (self.symbol,))
        rows_count = len(cur.fetchall())
        conn.close()
        return rows_count == 1


class ReutersDBEfficiencyTable(ReutersDBConnection):
    """
    insert, update, select and delete from efficiency table
    """
    def __init__(
            self,
            symbol,
            efficiency_name_box1,
            efficiency_company_box1,

            efficiency_industry_box1,
            efficiency_sector_box1,

            efficiency_name_box2,
            efficiency_company_box2,
            efficiency_industry_box2,
            efficiency_sector_box2,

            efficiency_name_box3,
            efficiency_company_box3,
            efficiency_industry_box3,
            efficiency_sector_box3,

            efficiency_name_box4,
            efficiency_company_box4,
            efficiency_industry_box4,
            efficiency_sector_box4,

            efficiency_name_box5,
            efficiency_company_box5,
            efficiency_industry_box5,
            efficiency_sector_box5,
            date_scrapped
    ):
        self.symbol = symbol
        self.efficiency_name_box1 = efficiency_name_box1
        self.efficiency_company_box1 = efficiency_company_box1
        self.efficiency_industry_box1 = efficiency_industry_box1
        self.efficiency_sector_box1 = efficiency_sector_box1
        self.efficiency_name_box2 = efficiency_name_box2
        self.efficiency_company_box2 = efficiency_company_box2
        self.efficiency_industry_box2 = efficiency_industry_box2
        self.efficiency_sector_box2 = efficiency_sector_box2
        self.efficiency_name_box3 = efficiency_name_box3
        self.efficiency_company_box3 = efficiency_company_box3
        self.efficiency_industry_box3 = efficiency_industry_box3
        self.efficiency_sector_box3 = efficiency_sector_box3
        self.efficiency_name_box4 = efficiency_name_box4
        self.efficiency_company_box4 = efficiency_company_box4
        self.efficiency_industry_box4 = efficiency_industry_box4
        self.efficiency_sector_box4 = efficiency_sector_box4
        self.efficiency_name_box5 = efficiency_name_box5
        self.efficiency_company_box5 = efficiency_company_box5
        self.efficiency_industry_box5 = efficiency_industry_box5
        self.efficiency_sector_box5 = efficiency_sector_box5
        self.date_scrapped = date_scrapped

    def insert_record_efficiency_table(self):

        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            insert into efficiency (
                symbol,
                efficiency_name_box1,
                efficiency_company_box1,

                efficiency_industry_box1,
                efficiency_sector_box1,

                efficiency_name_box2,
                efficiency_company_box2,
                efficiency_industry_box2,
                efficiency_sector_box2,

                efficiency_name_box3,
                efficiency_company_box3,
                efficiency_industry_box3,
                efficiency_sector_box3,

                efficiency_name_box4,
                efficiency_company_box4,
                efficiency_industry_box4,
                efficiency_sector_box4,

                efficiency_name_box5,
                efficiency_company_box5,
                efficiency_industry_box5,
                efficiency_sector_box5,
                date_scrapped
            )
            values (?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?,?)
        """
        cur.execute(
            sql_query, (
                self.symbol,
                self.efficiency_name_box1,
                self.efficiency_company_box1,
                self.efficiency_industry_box1,
                self.efficiency_sector_box1,
                self.efficiency_name_box2,
                self.efficiency_company_box2,
                self.efficiency_industry_box2,
                self.efficiency_sector_box2,
                self.efficiency_name_box3,
                self.efficiency_company_box3,
                self.efficiency_industry_box3,
                self.efficiency_sector_box3,
                self.efficiency_name_box4,
                self.efficiency_company_box4,
                self.efficiency_industry_box4,
                self.efficiency_sector_box4,
                self.efficiency_name_box5,
                self.efficiency_company_box5,
                self.efficiency_industry_box5,
                self.efficiency_sector_box5,
                self.date_scrapped
            )
        )
        conn.commit()
        conn.close()

    def update_record_efficiency_table(self):

        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            update efficiency
            set efficiency_name_box1=?,
                efficiency_company_box1=?,
                efficiency_industry_box1=?,
                efficiency_sector_box1=?,

                efficiency_name_box2=?,
                efficiency_company_box2=?,
                efficiency_industry_box2=?,
                efficiency_sector_box2=?,

                efficiency_name_box3=?,
                efficiency_company_box3=?,
                efficiency_industry_box3=?,
                efficiency_sector_box3=?,

                efficiency_name_box4=?,
                efficiency_company_box4=?,
                efficiency_industry_box4=?,
                efficiency_sector_box4=?,

                efficiency_name_box5=?,
                efficiency_company_box5=?,
                efficiency_industry_box5=?,
                efficiency_sector_box5=?
            where symbol=?
        """
        cur.execute(
            sql_query, (
                self.efficiency_name_box1,
                self.efficiency_company_box1,
                self.efficiency_industry_box1,
                self.efficiency_sector_box1,
                self.efficiency_name_box2,
                self.efficiency_company_box2,
                self.efficiency_industry_box2,
                self.efficiency_sector_box2,
                self.efficiency_name_box3,
                self.efficiency_company_box3,
                self.efficiency_industry_box3,
                self.efficiency_sector_box3,
                self.efficiency_name_box4,
                self.efficiency_company_box4,
                self.efficiency_industry_box4,
                self.efficiency_sector_box4,
                self.efficiency_name_box5,
                self.efficiency_company_box5,
                self.efficiency_industry_box5,
                self.efficiency_sector_box5,
                self.symbol
            )
        )
        conn.commit()
        conn.close()

    def symbol_in_efficiency_table(self):
        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            select id from efficiency where symbol=?
        """
        cur.execute(sql_query, (self.symbol,))
        rows_count = len(cur.fetchall())
        conn.close()
        return rows_count == 1


class ReutersDBManagementEffectivenessTable(ReutersDBConnection):
    """
    insert, update, select and delete from management_effectiveness table
    """
    def __init__(
            self,
            symbol,
            management_effectiveness_name_box1,
            management_effectiveness_company_box1,

            management_effectiveness_industry_box1,
            management_effectiveness_sector_box1,

            management_effectiveness_name_box2,
            management_effectiveness_company_box2,
            management_effectiveness_industry_box2,
            management_effectiveness_sector_box2,

            management_effectiveness_name_box3,
            management_effectiveness_company_box3,
            management_effectiveness_industry_box3,
            management_effectiveness_sector_box3,

            management_effectiveness_name_box4,
            management_effectiveness_company_box4,
            management_effectiveness_industry_box4,
            management_effectiveness_sector_box4,

            management_effectiveness_name_box5,
            management_effectiveness_company_box5,
            management_effectiveness_industry_box5,
            management_effectiveness_sector_box5,

            management_effectiveness_name_box6,
            management_effectiveness_company_box6,
            management_effectiveness_industry_box6,
            management_effectiveness_sector_box6,
            date_scrapped
    ):
        self.symbol = symbol
        self.management_effectiveness_name_box1 = management_effectiveness_name_box1
        self.management_effectiveness_company_box1 = management_effectiveness_company_box1
        self.management_effectiveness_industry_box1 = management_effectiveness_industry_box1
        self.management_effectiveness_sector_box1 = management_effectiveness_sector_box1
        self.management_effectiveness_name_box2 = management_effectiveness_name_box2
        self.management_effectiveness_company_box2 = management_effectiveness_company_box2
        self.management_effectiveness_industry_box2 = management_effectiveness_industry_box2
        self.management_effectiveness_sector_box2 = management_effectiveness_sector_box2
        self.management_effectiveness_name_box3 = management_effectiveness_name_box3
        self.management_effectiveness_company_box3 = management_effectiveness_company_box3
        self.management_effectiveness_industry_box3 = management_effectiveness_industry_box3
        self.management_effectiveness_sector_box3 = management_effectiveness_sector_box3
        self.management_effectiveness_name_box4 = management_effectiveness_name_box4
        self.management_effectiveness_company_box4 = management_effectiveness_company_box4
        self.management_effectiveness_industry_box4 = management_effectiveness_industry_box4
        self.management_effectiveness_sector_box4 = management_effectiveness_sector_box4
        self.management_effectiveness_name_box5 = management_effectiveness_name_box5
        self.management_effectiveness_company_box5 = management_effectiveness_company_box5
        self.management_effectiveness_industry_box5 = management_effectiveness_industry_box5
        self.management_effectiveness_sector_box5 = management_effectiveness_sector_box5
        self.management_effectiveness_name_box6 = management_effectiveness_name_box6
        self.management_effectiveness_company_box6 = management_effectiveness_company_box6
        self.management_effectiveness_industry_box6 = management_effectiveness_industry_box6
        self.management_effectiveness_sector_box6 = management_effectiveness_sector_box6
        self.date_scrapped = date_scrapped

    def insert_record_management_effectiveness_table(self):

        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            insert into management_effectiveness (
                symbol,
                management_effectiveness_name_box1,
                management_effectiveness_company_box1,

                management_effectiveness_industry_box1,
                management_effectiveness_sector_box1,

                management_effectiveness_name_box2,
                management_effectiveness_company_box2,
                management_effectiveness_industry_box2,
                management_effectiveness_sector_box2,

                management_effectiveness_name_box3,
                management_effectiveness_company_box3,
                management_effectiveness_industry_box3,
                management_effectiveness_sector_box3,

                management_effectiveness_name_box4,
                management_effectiveness_company_box4,
                management_effectiveness_industry_box4,
                management_effectiveness_sector_box4,

                management_effectiveness_name_box5,
                management_effectiveness_company_box5,
                management_effectiveness_industry_box5,
                management_effectiveness_sector_box5,

                management_effectiveness_name_box6,
                management_effectiveness_company_box6,
                management_effectiveness_industry_box6,
                management_effectiveness_sector_box6,
                date_scrapped
            )
            values (?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?,?,?)
        """
        cur.execute(
            sql_query, (
                self.symbol,
                self.management_effectiveness_name_box1,
                self.management_effectiveness_company_box1,
                self.management_effectiveness_industry_box1,
                self.management_effectiveness_sector_box1,
                self.management_effectiveness_name_box2,
                self.management_effectiveness_company_box2,
                self.management_effectiveness_industry_box2,
                self.management_effectiveness_sector_box2,
                self.management_effectiveness_name_box3,
                self.management_effectiveness_company_box3,
                self.management_effectiveness_industry_box3,
                self.management_effectiveness_sector_box3,
                self.management_effectiveness_name_box4,
                self.management_effectiveness_company_box4,
                self.management_effectiveness_industry_box4,
                self.management_effectiveness_sector_box4,
                self.management_effectiveness_name_box5,
                self.management_effectiveness_company_box5,
                self.management_effectiveness_industry_box5,
                self.management_effectiveness_sector_box5,
                self.management_effectiveness_name_box6,
                self.management_effectiveness_company_box6,
                self.management_effectiveness_industry_box6,
                self.management_effectiveness_sector_box6,
                self.date_scrapped
            )
        )
        conn.commit()
        conn.close()

    def update_record_management_effectiveness_table(self):

        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            update management_effectiveness
            set management_effectiveness_name_box1=?,
                management_effectiveness_company_box1=?,

                management_effectiveness_industry_box1=?,
                management_effectiveness_sector_box1=?,

                management_effectiveness_name_box2=?,
                management_effectiveness_company_box2=?,
                management_effectiveness_industry_box2=?,
                management_effectiveness_sector_box2=?,

                management_effectiveness_name_box3=?,
                management_effectiveness_company_box3=?,
                management_effectiveness_industry_box3=?,
                management_effectiveness_sector_box3=?,

                management_effectiveness_name_box4=?,
                management_effectiveness_company_box4=?,
                management_effectiveness_industry_box4=?,
                management_effectiveness_sector_box4=?,

                management_effectiveness_name_box5=?,
                management_effectiveness_company_box5=?,
                management_effectiveness_industry_box5=?,
                management_effectiveness_sector_box5=?,

                management_effectiveness_name_box6=?,
                management_effectiveness_company_box6=?,
                management_effectiveness_industry_box6=?,
                management_effectiveness_sector_box6=?
            where symbol=?
        """
        cur.execute(
            sql_query, (
                self.management_effectiveness_name_box1,
                self.management_effectiveness_company_box1,
                self.management_effectiveness_industry_box1,
                self.management_effectiveness_sector_box1,
                self.management_effectiveness_name_box2,
                self.management_effectiveness_company_box2,
                self.management_effectiveness_industry_box2,
                self.management_effectiveness_sector_box2,
                self.management_effectiveness_name_box3,
                self.management_effectiveness_company_box3,
                self.management_effectiveness_industry_box3,
                self.management_effectiveness_sector_box3,
                self.management_effectiveness_name_box4,
                self.management_effectiveness_company_box4,
                self.management_effectiveness_industry_box4,
                self.management_effectiveness_sector_box4,
                self.management_effectiveness_name_box5,
                self.management_effectiveness_company_box5,
                self.management_effectiveness_industry_box5,
                self.management_effectiveness_sector_box5,
                self.management_effectiveness_name_box6,
                self.management_effectiveness_company_box6,
                self.management_effectiveness_industry_box6,
                self.management_effectiveness_sector_box6,
                self.symbol
            )
        )
        conn.commit()
        conn.close()

    def symbol_in_management_effectiveness_table(self):
        conn = self._connect()
        cur = conn.cursor()
        sql_query = """
            select id from management_effectiveness where symbol=?
        """
        cur.execute(sql_query, (self.symbol,))
        rows_count = len(cur.fetchall())
        conn.close()
        return rows_count == 1