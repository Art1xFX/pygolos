import json
import struct

from varint import encode


class Rate:
    def __init__(self,
                 author: str,
                 permlink: str,
                 value: int):
        self.author = author
        self.permlink = permlink
        self.value = value

    def binarify(self):
        buffer = b""
        buffer += (encode(len(self.author)) + bytes(self.author, "utf-8"))
        buffer += (encode(len(self.permlink)) + bytes(self.permlink, "utf-8"))
        #buffer += struct.pack("<i", self.value)
        buffer += bytes([self.value])
        return buffer

    def jsonify(self):
        return json.dumps(self.__dict__)