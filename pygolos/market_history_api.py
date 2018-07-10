import json


class MarketHistoryApi:
    def __init__(self, api):
        self.__api = api

    def get_ticker(self):
        """
        Returns the market ticker for the internal GBD:GOLOS market.
        :return:
        """
        return self.__api._Api__call("market_history","get_ticker",[])

    def get_volume(self):
        """
        Returns the market volume for the past 24 hours.
        :return:
        """
        return self.__api._Api__call("market_history","get_volume",[])

    def get_order_book(self,limit:int):
        """

        Returns the internal market order book.
        :param limit:int
        :return:
        """
        if limit>500 or limit<0:
            raise TypeError
        return self.__api._Api__call("market_history","get_order_book",[limit])

    def get_order_book_extended(self,limit:int):
        """

        Returns the extended internal market order book.
        :param limit:int
        :return:
        """
        if limit>500 or limit<0:
            raise TypeError
        return self.__api._Api__call("market_history","get_order_book_extended",[limit])

    def get_trade_history(self,start:str,end:str,limit:int):
        """
        Returns the trade history for the internal GBD:GOLOS market.
        :param start: data type
        :param end: data type
        :param limit:
        """
        return self.__api._Api__call("market_history","get_trade_history",[start,end,limit])


    def get_recent_trades(self,limit:int):
        """

        Returns recent transactions
        :param limit:int
        :return:
        """
        if limit>500 or limit<0:
            raise TypeError
        return self.__api._Api__call("market_history","get_recent_trades",[limit])

    def get_market_history(self,bucket_seconds,start,end):
        """
        Returns the market history for the internal GBD: GOLOS market
        :param bucket_seconds: int
        :param start:time format
        :param end: time format
        """
        return self.__api._Api__call("market_history", "get_market_history", [bucket_seconds,start,end])

    def get_market_history_buckets(self):
        """

        Returns the bucket seconds being tracked by the plugin.
        """
        return self.__api._Api__call("market_history", "get_market_history_buckets", [])

    def get_open_orders(self,owner:str):
        """
        Returns the open orders for an account.
        :param owner: String
        """
        return self.__api._Api__call("market_history","get_open_orders",[owner])
