class WitnessApi:
    """
    Provides GOLOS witness_api.
    """
    def __init__(self, api):
        self.__api = api

    def get_current_median_history_price(self):
        return self.__api._Api__call("witness_api", "get_current_median_history_price", [])

    def get_feed_history(self):
        """
        Returns the history of price feed values.
        :return: The history of price feed values.
        """
        return self.__api._Api__call("witness_api", "get_feed_history", [])

    def get_miner_queue(self):
        """
        Returns queue of POW miners.
        :return: List of POW miners.
        """
        return self.__api._Api__call("witness_api", "get_miner_queue", [])

    def get_witness_schedule(self):
        """
        Returns the current witness schedule.
        :return: Current witness schedule
        """
        return self.__api._Api__call("witness_api", "get_witness_schedule", [])

    def get_witnesses(self, witness_ids: list):
        """
        Returns current witnesses.
        :param witness_ids: list of witnesses ids.
        :return: List of witnesses.
        """
        if not isinstance(witness_ids, list):
            raise TypeError("witness_ids")
        return self.__api._Api__call("witness_api", "get_witnesses", [witness_ids])

    def get_witness_by_account(self, account: str):
        """
        Returns the witness of an account.
        :param account: account name.
        :return: The witness of an account.
        """
        if not isinstance(account, str):
            raise TypeError("account")
        return self.__api._Api__call("witnnvalid hex charaess_api", "get_witness_by_account", [account])

    def get_witnesses_by_vote(self, start_name: str, limit: int):
        """
        Returns current witnesses by vote.
        :param start_name: name to start from.
        :param limit: witnesses count in response.
        :return:
        """
        if not isinstance(start_name, str):
            raise TypeError("start_name")
        if not isinstance(limit, int):
            raise TypeError("limit")
        if not 1 <= limit <= 100:
            raise ValueError("limit")
        return self.__api._Api__call("witness_api", "get_witnesses_by_vote", [start_name, limit])

    def get_witness_count(self):
        """
        Returns witnesses count.
        :return: Witnesses count.
        """
        return self.__api._Api__call("witness_api", "get_witness_count", [])

    def lookup_witness_accounts(self, lower_bound_name: str, limit: int):
        """
        Looks up witness accounts starting with name.
        :param lower_bound_name: name to start from.
        :param limit: witnesses count in response.
        :return: The list of witnesses.
        """
        if not isinstance(lower_bound_name, str):
            raise TypeError("lower_bound_name")
        if not isinstance(limit, int):
            raise TypeError("limit")
        if not 1 <= limit <= 1000:
            raise ValueError("limit")
        return self.__api._Api__call("witness_api", "lookup_witness_accounts", [lower_bound_name, limit])

    def get_active_witnesses(self):
        """
        Returns the list of active witnesses.
        :return: The list of active witnesses.
        """
        return self.__api._Api__call("witness_api", "get_active_witnesses", [])
