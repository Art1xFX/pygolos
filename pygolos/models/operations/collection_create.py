import json
import struct

from varint import encode
from pygolos.utils.asset import Asset

class CollectionCreate:

    def __init__(self,
                 author: str,
                 permlink: str,
                 title: str,
                 price: str,
                 quantity: int):
        self.author = author
        self.permlink = permlink
        self.title = title
        self.price = price
        self.quantity = quantity

    def binarify(self):
        buffer = b""
        buffer += (encode(len(self.author)) + bytes(self.author, "utf-8"))
        buffer += (encode(len(self.permlink)) + bytes(self.permlink, "utf-8"))
        buffer += (encode(len(self.title)) + bytes(self.title, "utf-8"))
        buffer += Asset(self.price).__bytes__()
        buffer += struct.pack("i", self.quantity)
        return buffer

    def jsonify(self):
        return json.dumps(self.__dict__)

    def __str__(self):
        return "collection_create"
