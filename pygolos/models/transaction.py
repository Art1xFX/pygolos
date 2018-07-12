import struct
import time
from calendar import timegm
from json import dumps

import varint

_operations = {"vote": b"\0", "comment": b"1"}

class Transaction:
    def __init__(self,
                 ref_block_num: int = int(),
                 ref_block_prefix: int = int(),
                 expiration: str=str(),
                 operations: list = list()):
        self.ref_block_num = ref_block_num
        self.ref_block_prefix = ref_block_prefix
        self.expiration = expiration
        self.operations = operations
        self.extensions = []
        self.signatures = []

    def binarify(self):
        buffer = b""
        buffer += struct.pack("<H", self.ref_block_num)
        buffer += struct.pack("<I", self.ref_block_prefix)
        buffer += struct.pack("<I", timegm(time.strptime((self.expiration + "UTC"), "%Y-%m-%dT%H:%M:%S%Z")))
        buffer += bytes(varint.encode(len(self.operations)))
        for op in self.operations:
            buffer += _operations[op.__class__.__name__.lower()]
            buffer += op.binarify()
        buffer += bytes(varint.encode(len(self.extensions)))
        return buffer


    def jsonify(self):
        obj = self.__dict__.copy()
        obj["operations"] = [[op.__class__.__name__.lower(), op.__dict__] for op in self.operations]
        return dumps(obj)

