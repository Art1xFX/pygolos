
class MarketPlaceApi:

    def __init__(self, api):
        self.__api = api

    def get_lots(self):
        return self.__api._Api__call("market_place_api", "get_lots", [])

    def get_lots_by_account(self, account: str):
        return self.__api._Api__call("market_place_api", "get_lots_by_account", [account])

    def get_lots_by_permlink(self, permlink: str):
        return self.__api._Api__call("market_place_api", "get_lots_by_permlink", [permlink])

    def get_trades_by_from(self, account: str):
        return self.__api._Api__call("market_place_api", "get_trades_by_from", [account])

    def get_trades_by_to(self, account: str):
        return self.__api._Api__call("market_place_api", "get_trades_by_to", [account])

    def get_trades_by_permlink(self, permlink: str):
        return self.__api._Api__call("market_place_api", "get_trades_by_permlink", [permlink])
