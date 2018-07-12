import hashlib
import struct
from calendar import timegm
import datetime

import time
from binascii import unhexlify, hexlify
from  pygolos.models import Transaction
import ecdsa as ecdsa
import pygolos
import string


import varint as varint


class ApiHelper:
    def __init__(self, api: pygolos.Api):
        self.__api = api

    def create_post(self):
        pass

    def like(self, posting_key, voter, author, permlink, weight):
        dgp = self.__api.database_api.get_dynamic_global_properties()["result"]
        op = pygolos.models.operations.Vote(voter, author, permlink, weight)
        t = datetime.datetime.utcnow() + datetime.timedelta(seconds=4)
        trx = Transaction(ref_block_num=dgp["head_block_number"] & 0xFFFF,
                          ref_block_prefix=struct.unpack_from("<I", unhexlify(dgp["head_block_id"]), 4)[0],
                          expiration=t.strftime("%Y-%m-%dT%H:%M:%S%Z"),
                          operations=[op])
        trx.sign([posting_key])
        return self.__api.network_broadcast_api.broadcast_transaction_synchronous(trx)

    def post(self,
             key,
             parent_permlink: str=str(),
             author: str=str(),
             permlink: str=str(),
             title: str=str(),
             body: str=str(),
             json_metadata: str=str()):
        dgp = self.__api.database_api.get_dynamic_global_properties()["result"]
        op = pygolos.models.operations.Comment(parent_author="",
                                               parent_permlink=parent_permlink,
                                               author=author,
                                               permlink=permlink,
                                               title=title,
                                               body=body,
                                               json_metadata=json_metadata)
        t = datetime.datetime.utcnow() + datetime.timedelta(seconds=4)
        trx = Transaction(ref_block_num=dgp["head_block_number"] & 0xFFFF,
                          ref_block_prefix=struct.unpack_from("<I", unhexlify(dgp["head_block_id"]), 4)[0],
                          expiration=t.strftime("%Y-%m-%dT%H:%M:%S%Z"),
                          operations=[op])
        trx.sign([key])
        return self.__api.network_broadcast_api.broadcast_transaction_synchronous(trx)

    def comment(self,
             key,
             parent_author: str=str(),
             parent_permlink: str=str(),
             author: str=str(),
             permlink: str=str(),
             title: str=str(),
             body: str=str(),
             json_metadata: str=str()):
        dgp = self.__api.database_api.get_dynamic_global_properties()["result"]
        op = pygolos.models.operations.Comment(parent_author=parent_author,
                                               parent_permlink=parent_permlink,
                                               author=author,
                                               permlink=permlink,
                                               title=title,
                                               body=body,
                                               json_metadata=json_metadata)
        t = datetime.datetime.utcnow() + datetime.timedelta(seconds=4)
        trx = Transaction(ref_block_num=dgp["head_block_number"] & 0xFFFF,
                          ref_block_prefix=struct.unpack_from("<I", unhexlify(dgp["head_block_id"]), 4)[0],
                          expiration=t.strftime("%Y-%m-%dT%H:%M:%S%Z"),
                          operations=[op])
        trx.sign([key])
        return self.__api.network_broadcast_api.broadcast_transaction_synchronous(trx)
