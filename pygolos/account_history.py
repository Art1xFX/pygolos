class AccountHistory:
    """
    Provides GOLOS account_history api.
    """
    def __init__(self, api):
        self.__api = api

    def get_account_history(self, account: str, start: int, limit: int):
        """
        Returns a history of all operations for a given account.
        :param account: account name.
        :param start:
        :param limit: operations count in response.
        :return: A history of all operations for a given account.
        """
        if not isinstance(account, str):
            raise TypeError("account")
        if not isinstance(start, int):
            raise TypeError("start")
        if not isinstance(limit, int):
            raise TypeError("limit")
        if not 1 <= limit <= 100:
            raise ValueError("limit")
        return self.__api._Api__call("account_history", "get_account_history", [account, start, limit])
