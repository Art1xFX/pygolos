class WitnessApi:
    def __init__(self, api):
        self.__api = api

    def get_current_median_history_price(self):
        return self.__api._Api__call("witness_api", "get_current_median_history_price", [])
