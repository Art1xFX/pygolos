from websocket import create_connection
from json import dumps
from json import loads

from pygolos.database_api import DatabaseApi
from pygolos.witness_api import WitnessApi


class Api:
    def __init__(self, url="wss://ws.golos.io"):
        self.__ws = create_connection(url)
        self._witness = WitnessApi(self)
        self._database=DatabaseApi(self)

    @property
    def witness(self):
        return self._witness

    @property
    def database(self):
        return self._database

    @property
    def account_history(self):
        pass

    def __call(self, api, method, params):
        self.__ws.send(dumps({"method": "call", "jsonrpc": "2.0",
                              "params": [api, method, params]}))
        return loads(self.__ws.recv())
