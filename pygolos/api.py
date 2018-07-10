from websocket import create_connection
from json import dumps
from json import loads
from pygolos.witness_api import WitnessApi
from pygolos.account_history import AccountHistory
from pygolos.operation_history import OperationHistory
from pygolos.tags import Tags
from pygolos.social_network import SocialNetwork
from pygolos.account_by_key import AccountByKey
from pygolos.database_api import DatabaseApi
from pygolos.follow_api import FollowApi
from pygolos.network_broadcast_api import NetworkBroadcastApi


class Api:
    def __init__(self, url="wss://ws.golos.io"):
        self.__ws = create_connection(url)
        self.__witness = WitnessApi(self)
        self.__account_history = AccountHistory(self)
        self.__operation_history = OperationHistory(self)
        self.__tags = Tags(self)
        self.__social_network = SocialNetwork(self)
        self.__account_by_key = AccountByKey(self)
        self.__database_api = DatabaseApi(self)
        self.__follow_api = FollowApi(self)
        self.__network_broadcast_api = NetworkBroadcastApi(self)

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

    def __call(self, api, method, params):
        self.__ws.send(dumps({"method": "call", "jsonrpc": "2.0",
                              "params": [api, method, params]}))
        return loads(self.__ws.recv())
