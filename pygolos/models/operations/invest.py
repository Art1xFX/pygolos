import json
import struct

from varint import encode


class Invest:
    def __init__(self,
                 investor: str,
                 permlink: str,
                 quantity: int):
        self.investor = investor
        self.permlink = permlink
        self.quantity = quantity

    def binarify(self):
        buffer = b""
        buffer += (encode(len(self.investor)) + bytes(self.investor, "utf-8"))
        buffer += (encode(len(self.permlink)) + bytes(self.permlink, "utf-8"))
        buffer += struct.pack("i", self.quantity)
        return buffer

    def jsonify(self):
        return json.dumps(self.__dict__)

    def __str__(self):
        return "invest"