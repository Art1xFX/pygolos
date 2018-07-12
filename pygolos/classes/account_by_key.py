class AccountByKey:
    """
    Provides GOLOS account_by_key classes.
    """
    def __init__(self, api):
        self.__api = api

    def get_key_references(self, keys: list):
        """
        Returns all accounts that have the key associated with their owner or active authorities.
        :param key: account keys.
        :return: Accounts list.
        """
        if not isinstance(keys, list):
            raise TypeError("key")
        return self.__api._Api__call("account_by_key", "get_key_references", [keys])
