class DatabaseApi:
    def __init__(self, api):
        self.__api = api

    def get_block_header(self, blockNum:int):
        """
        Displays brief information on the specified block.
        :param blockNum: block number(uint32_t)

        """
        return self.__api._Api__call("database_api", "get_block_header", [blockNum])

    def get_block(self, blockNum:int):
        """
        Displays extended information for the specified block.
        :param blockNum: block number(uint32_t)

        """

        return self.__api._Api__call("database_api", "get_block", [blockNum])

    def get_config(self):
        """
        Displays the current node configuration.
        """
        return self.__api._Api__call("database_api", "get_config", [])

    def get_dynamic_global_properties(self):
        """
        Displays various information about the current status of the GOLOS network.
        """
        return self.__api._Api__call("database_api", "get_dynamic_global_properties", [])

    def get_chain_properties(self):
        """
        Displays the commission for creating the user, the maximum block size and the GBG interest rate.
        """
        return self.__api._Api__call("database_api", "get_chain_properties", [])

    def get_hardfork_version(self):
        """
        Displays the current version of GOLOS.
        """
        return self.__api._Api__call("database_api", "get_hardfork_version", [])

    def get_next_scheduled_hardfork(self):
        """
        Displays the date and version of GOLOS
        """
        return self.__api._Api__call("database_api", "get_next_scheduled_hardfork", [])

    def get_account_count(self):
        """
        Shows the number of users registered in the GOLOS network.
        """
        return self.__api._Api__call("database_api", "get_account_count", [])

    def get_owner_history(self, account:str):
        """
        Displays the user name if he changed the ownership of the block.
        :param account: Username (string)
        """
        return self.__api._Api__call("database_api", "get_owner_history", [account])

    def get_recovery_request(self, account:str):
        """
        If the user status is currently marked for recovery, it returns true, otherwise "null" is returned.
        :param account:Username(string)
        """
        return self.__api._Api__call("database_api", "get_recovery_request", [account])

    def get_escrow(self, after, escrowId:int):
        """
        Returns the escrow for a certain account by id.
        :param after:
        :param escrowId:int
        :return:
        """
        return self.__api._Api__call("database_api", "get_recovery_request", [frm, escrowId])

    def get_withdraw_routes(self, account, withdrw):
        """
        the command issues user translations, depending on the type incoming, outgoing or all.
        :param account:Username(string)
        :param withdrw: Type "incoming", "outgoing" or "all".
        :return:
        """
        return self.__api._Api__call("database_api", "get_withdraw_routes", [account, withdrw])

    def get_account_bandwidth(self, account:str, bandwidthType:int):
        """

        :param account:Username(string)
        :param bandwidthType: int 0-4
        :return:
        """
        if bandwidthType<0 or bandwidthType>4:
            raise TypeError
        return self.__api._Api__call("database_api", "get_account_bandwidth", [account, bandwidthType])

    def get_savings_withdraw_from(self, account:str):
        """
       Returns savings withdraw from an account.
        :param account:string
        :return:
        """
        return self.__api._Api__call("database_api", "get_savings_withdraw_from", [account])

    def get_savings_withdraw_to(self, account:str):
        """
        Returns the savings withdraw to an account.
        :param account:Username(string)
        :return:
        """
        return self.__api._Api__call("database_api", "get_savings_withdraw_to", [account])

    def get_conversion_requests(self, accountName:str):
        """
        Displays current requests for conversion by the specified user.
        :param accountName:
        :return:
        """
        return self.__api._Api__call("database_api", "get_conversion_requests", [accountName])

    def get_transaction_hex(self, trx:str):
        """
        Returns a hexdump of the serialized binary form of a transaction.
        :param trx:Serialized hex form
  "trx": {
    "ref_block_num": 0,
    "ref_block_prefix": 0,
    "expiration": "1970-01-01T00:00:00",
    "operations": [],
    "extensions": [],
    "signatures": []
  }
}
        :return:
        """
        return self.__api._Api__call("database_api", "get_transaction_hex", [trx])

    def get_required_signatures(self, trx:str, availableKeys):
        """

        This API will take a partially signed transaction and a set of public keys that the owner has the ability to sign for and return the minimal subset of public keys that should add signatures to the transaction.
        :param trx:Serialized hex form
  "trx": {
    "ref_block_num": 0,
    "ref_block_prefix": 0,
    "expiration": "1970-01-01T00:00:00",
    "operations": [],
    "extensions": [],
    "signatures": []
  }
}
        :param availableKeys:???
        :return:
        """
        return self.__api._Api__call("database_api", "get_required_signatures", [trx, availableKeys])

    def get_potential_signatures(self, trx):
        """
        This method will return the set of all public keys that could possibly sign for a given transaction.
        :param trx:Serialized
        {
  "trx": {
    "ref_block_num": 0,
    "ref_block_prefix": 0,
    "expiration": "1970-01-01T00:00:00",
    "operations": [],
    "extensions": [],
    "signatures": []
  }
}
        :return:
        """
        return self.__api._Api__call("database_api", "get_potential_signatures", [trx])

    def verify_authority(self, trx):
        """
        Returns true if the transaction has all of the required signatures.
        :param trx:Serialized
        {
  "trx": {
    "ref_block_num": 0,
    "ref_block_prefix": 0,
    "expiration": "1970-01-01T00:00:00",
    "operations": [],
    "extensions": [],
    "signatures": []
  }
}
        :return:
        """
        return self.__api._Api__call("database_api", "verify_authority", [trx])

    def verify_account_authority(self, name, signers):
        """
        Not implemented
        :param name: String ??
        :param signers: String ??
        :return:
        """
        return self.__api._Api__call("database_api", "verify_account_authority", [name, signers])

    def get_accounts(self, accountNames:list):
        """
        Displays information about the users specified in the request.
        :param accountNames:List type
        :return:
        """
        return self.__api._Api__call("database_api", "get_accounts", [accountNames])

    def lookup_account_names(self, accountNames):
        """
        Displays information about the users specified in the request.
        :param accountNames:List type
        :return:
        """
        return self.__api._Api__call("database_api", "lookup_account_names", [accountNames])

    def lookup_accounts(self, lowerBoundName, limit:int):
        """
        Returns list of all users which contains lowerBoundName
        :param lowerBoundName: String
        :param limit: int >0
        :return:
        """
        if limit<0:
            raise TypeError
        return self.__api._Api__call("database_api", "lookup_accounts", [lowerBoundName, limit])


    def get_database_info(self):
        """
        Displays info about GOLOS database
        :return:
        """
        return self.__api._Api__call("database_api", "get_database_info", [])

    def get_vesting_delegations(self, account:str, after, limit:int, tpe):
        """
        Returns the vesting delegations by an account
        :param account:String
        :param after:Time format
        :param limit:int>=0
        :param tpe:int??
        :return:
        """
        if limit<0 or limit>10:
            raise TypeError
        return self.__api._Api__call("database_api", "get_vesting_delegations", [account, after, limit, tpe])

    def get_expiring_vesting_delegations(self, account:str, after, limit:int):
        """
        Returns the expiring vesting delegations for an account.
        :param account:String
        :param after:Time format
        :param limit:int>=0
        :return:
        """
        if limit<0 or limit>10:
            raise TypeError
        return self.__api._Api__call("database_api", "get_expiring_vesting_delegations", [account, after, limit])
