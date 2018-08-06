import json
import struct

from varint import encode


class Collection():

    def __init__(self,
                 author: str=str(),
                 permlink: str=str(),
                 title: str=str()):
        self.author = author
        self.permlink = permlink
        self.title = title

    def binarify(self):
        buffer = b""
        buffer += (encode(len(self.author)) + bytes(self.author, "utf-8"))
        buffer += (encode(len(self.permlink)) + bytes(self.permlink, "utf-8"))
        buffer += (encode(len(self.title)) + bytes(self.title, "utf-8"))
        return buffer

    def jsonify(self):
        return json.dumps(self.__dict__)