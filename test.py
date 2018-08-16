import struct
import time
from binascii import unhexlify

from pygolos import Api
from pygolos import ApiHelper

import json
from pygolos.models.operations import Vote
from pygolos.models import Transaction, Query
from json import dumps

def get_info(accounts):
    for a in accounts:
        acc = api.database_api.get_accounts([a])["result"][0]
        print(a + ": " + acc["balance"] + "   " + acc["balances"].__str__())


if __name__ == '__main__':
    # api = Api()
    api = Api(url="ws://192.168.5.103:8091")
    # api = Api()
    helper = ApiHelper(api)
    Api.chain_id = "5876894a41e6361bde2e73278f07340f2eb8b41c2facd29099de9deef6cdb679"

    # 5JVFFWRLwz6JoP9kguuRFfytToGU6cLgBVTL9t6NB3D3BQLbUBS
    #print(helper.collection_create("5JrFCm5Ka7QMztXx8Fw9juY8xz3yQYbuMgSe3etdmkv49KJa2xi", "roma", "MDCRAW2017",
    #                               "Cricova", "300.000 GOLOS", 1000))
    print(api.collection_api.get_collection("MDCRAW2017"))
    #print(helper.invest("5Hq3VC2hVeW7p52TfHLZhpw7343LVKn4a17t3d9BP9wYYr3qyzK", "jora", "MDCRAW2017", 5))


    print(api.market_place_api.get_trades_by_permlink("MDCRAW2017"))

    #print(api.collection_api.get_investments_by_investor("evlampiia"))
