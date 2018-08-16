import json
import struct

from varint import encode


class Buy:
    def __init__(self,
                 account: str,
                 owner: str,
                 permlink: str,
                 quantity: int):
        self.account = account
        self.owner = owner
        self.permlink = permlink
        self.quantity = quantity

    def binarify(self):
        buffer = b""
        buffer += (encode(len(self.account)) + bytes(self.account, "utf-8"))
        buffer += (encode(len(self.owner)) + bytes(self.owner, "utf-8"))
        buffer += (encode(len(self.permlink)) + bytes(self.permlink, "utf-8"))
        buffer += struct.pack("i", self.quantity)
        return buffer

    def jsonify(self):
        return json.dumps(self.__dict__)

    def __str__(self):
        return "buy"