import struct

from varint import encode


class Vote():

    def __init__(self, voter: str=str(), author: str=str(), permlink: str=str(), weight: int=int()):
        self.voter = voter
        self.author = author
        self.permlink = permlink
        self.weight = weight

    def binarify(self):
        buffer = b""
        buffer += (encode(len(self.voter)) + bytes(self.voter, "utf-8"))
        buffer += (encode(len(self.author)) + bytes(self.author, "utf-8"))
        buffer += (encode(len(self.permlink)) + bytes(self.permlink, "utf-8"))
        buffer += struct.pack("<h", int(self.weight))
        return buffer


    def jsonify(self):
        return ""

    def __str__(self):
        return "vote"