import json
import struct

from varint import encode
from pygolos.utils.asset import Asset

class Cancel:
    def __init__(self,
                 account: str,
                 permlink: str):
        self.account = account
        self.permlink = permlink

    def binarify(self):
        buffer = b""
        buffer += (encode(len(self.account)) + bytes(self.account, "utf-8"))
        buffer += (encode(len(self.permlink)) + bytes(self.permlink, "utf-8"))
        return buffer

    def jsonify(self):
        return json.dumps(self.__dict__)

    def __str__(self):
        return "cancel"