from websocket import create_connection
from json import dumps
from json import loads
from pygolos.witness_api import WitnessApi
from pygolos.account_history import AccountHistory
from pygolos.operation_history import OperationHistory
from pygolos.tags import Tags


class Api:
    def __init__(self, url="wss://ws.golos.io"):
        self.__ws = create_connection(url)
        self.__witness = WitnessApi(self)
        self.__account_history = AccountHistory(self)
        self.__operation_history = OperationHistory(self)
        self.__tags = Tags(self)

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

    def __call(self, api, method, params):
        self.__ws.send(dumps({"method": "call", "jsonrpc": "2.0",
                              "params": [api, method, params]}))
        return loads(self.__ws.recv())
