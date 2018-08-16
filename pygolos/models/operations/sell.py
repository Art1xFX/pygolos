import json
import struct

from varint import encode
from pygolos.utils.asset import Asset

class Sell:
    def __init__(self,
                 account: str,
                 permlink: str,
                 price: str,
                 quantity: int):
        self.account = account
        self.permlink = permlink
        self.price = price
        self.quantity = quantity

    def binarify(self):
        buffer = b""
        buffer += (encode(len(self.account)) + bytes(self.account, "utf-8"))
        buffer += (encode(len(self.permlink)) + bytes(self.permlink, "utf-8"))
        buffer += Asset(self.price).__bytes__()
        buffer += struct.pack("i", self.quantity)
        return buffer

    def jsonify(self):
        return json.dumps(self.__dict__)

    def __str__(self):
        return "sell"