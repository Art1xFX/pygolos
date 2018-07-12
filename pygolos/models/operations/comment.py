import json
import struct

from varint import encode


class Comment():

    def __init__(self,
                 parent_author: str=str(),
                 parent_permlink: str=str(),
                 author: str=str(),
                 permlink: str=str(),
                 title: str=str(),
                 body: str=str(),
                 json_metadata: str=str()):
        self.parent_author = parent_author
        self.author = author
        self.permlink = permlink
        self.parent_permlink = parent_permlink
        self.title = title
        self.body = body
        self.json_metadata = json_metadata

    def binarify(self):
        buffer = b""
        buffer += (encode(len(self.parent_author)) + bytes(self.parent_author, "utf-8"))
        buffer += (encode(len(self.parent_permlink)) + bytes(self.parent_permlink, "utf-8"))
        buffer += (encode(len(self.author)) + bytes(self.author, "utf-8"))
        buffer += (encode(len(self.permlink)) + bytes(self.permlink, "utf-8"))
        buffer += (encode(len(self.title)) + bytes(self.title, "utf-8"))
        buffer += (encode(len(self.body)) + bytes(self.body, "utf-8"))
        buffer += (encode(len(self.json_metadata)) + bytes(self.json_metadata, "utf-8"))
        return buffer

    def jsonify(self):
        return json.dumps(self.__dict__)
