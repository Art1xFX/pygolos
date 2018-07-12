from websocket import create_connection
from json import dumps
from json import loads
from pygolos.classes import database_api, network_broadcast_api, tags, account_by_key, account_history, follow_api, \
    operation_history, social_network, witness_api, market_history_api


class Api:
    def __init__(self, url="wss://ws.golos.io", chain_id: str="782a3039b478c839e4cb0c941ff4eaeb7df40bdd68bd441afd444b9da763de12"):
        self.__ws = create_connection(url)
        self.url = url
        self.chain_id = chain_id
        self.__witness = witness_api.WitnessApi(self)
        self.__account_history = account_history.AccountHistory(self)
        self.__operation_history = operation_history.OperationHistory(self)
        self.__tags = tags.Tags(self)
        self.__social_network = social_network.SocialNetwork(self)
        self.__account_by_key = account_by_key.AccountByKey(self)
        self.__database_api = database_api.DatabaseApi(self)
        self.__follow_api = follow_api.FollowApi(self)
        self.__network_broadcast_api = network_broadcast_api.NetworkBroadcastApi(self)
        self.__market_history = market_history_api.MarketHistoryApi(self)

    @property
    def witness(self):
        return self.__witness

    @property
    def account_history(self):
        return self.__account_history

    @property
    def operation_history(self):
        return self.__operation_history

    @property
    def tags(self):
        return self.__tags
    
    @property
    def social_network(self):
        return self.__social_network

    @property
    def account_by_key(self):
        return self.__account_by_key

    @property
    def database_api(self):
        return self.__database_api

    @property
    def follow_api(self):
        return self.__follow_api

    @property
    def network_broadcast_api(self):
        return self.__network_broadcast_api

    @property
    def market_history(self):
        return self.__market_history

    def __call(self, api, method, params):
        self.__ws.send(dumps({"method": "call", "jsonrpc": "2.0",
                              "params": [api, method, params]}))
        return loads(self.__ws.recv())