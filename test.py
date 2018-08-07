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

    # 5JVFFWRLwz6JoP9kguuRFfytToGU6cLgBVTL9t6NB3D3BQLbUBS

    # print(helper.collection("5JVFFWRLwz6JoP9kguuRFfytToGU6cLgBVTL9t6NB3D3BQLbUBS", "gustosminer", "MDCRAW2017", "Cricova"))
    # print(helper.rate("5JER8gCJYN3g9LrwyMiEde2g4u8UjUYUctRva1BFf64bUM9omqF", "equinox", "MDCRAW2017", 3))
    # print(helper.rate("5KBsFyLnJPeBdLHncELWfT6NowT9b7C7Qf6hJXzVnscAcnuK6Cg", "fake", "MDCRAW2017", 4))
    # print(api.collection_api.get_collection("MDCRAW2017"))
    print(api.collection_api.get_collection_marks("MDCRAW2017"))


