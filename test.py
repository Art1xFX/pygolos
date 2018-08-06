import struct
import time
from binascii import unhexlify

from pygolos import Api
from pygolos import ApiHelper

import json
from pygolos.models.operations import Vote
from pygolos.models import Transaction, Query
from json import dumps


if __name__ == '__main__':
    # api = Api()
    api = Api(url="ws://192.168.5.103:8091")
    # api = Api()
    helper = ApiHelper(api)
    Api.chain_id = "5876894a41e6361bde2e73278f07340f2eb8b41c2facd29099de9deef6cdb679"
    """
    {'jsonrpc': '2.0', 'result': {'id': '82ec5b3b25fc2ea44c4d471a5f27e0247277181b', 'block_num': 1801, 'trx_num': 0, 'expired': False}, 'id': None}
    """
    # print(api.database_api.get_block(63))
    # print(helper.collection("5JVFFWRLwz6JoP9kguuRFfytToGU6cLgBVTL9t6NB3D3BQLbUBS", "gustosminer", "prm", "my collec"))
    print(api._Api__call("collection_api", "get_collection", ["gustosminer", "prm"]))
    #print(helper.collection("5JVFFWRLwz6JoP9kguuRFfytToGU6cLgBVTL9t6NB3D3BQLbUBS", "gustosminer", "mycol", "mytitle"))

    # print(api.social_network.get_content("fake", "mypost229", 10))
"""
    metadata = {"tags": ["fake", "wine"], "format": "HTML", "image": "http://example.com/1.jpg"}

    print(helper.post('5JVFFWRLwz6JoP9kguuRFfytToGU6cLgBVTL9t6NB3D3BQLbUBS',
                         "white",
                         "fake",
                         "mypost229",
                         "Very interesting post",
                         "<h2>The most intresting post too</h2>The another one useless post 124.", json.dumps(metadata)))
"""

    #json.dumps(metadata)

