class OperationHistory:
    """
    Provides GOLOS operation_history api.
    """
    def __init__(self, api):
        self.__api = api

    def get_ops_in_block(self, block_num: int, only_virtual: bool):
        """
        Returns all operations contained in a block.
        :param block_num: block number.
        :param only_virtual:
        :return: List of operations.
        """
        if not isinstance(block_num, int):
            raise TypeError("block_num")
        if not isinstance(only_virtual, bool):
            raise TypeError("only_virtual")
        return self.__api._Api__call("operation_history", "get_ops_in_block", [block_num, only_virtual])

    def get_transaction(self, trx_id: int):
        """
        Returns the details of a transaction based on a transaction id.
        :param trx_id: transaction id.
        :return: The details of a transaction based on a transaction id.
        """
        if not isinstance(trx_id, int):
            raise TypeError("id")
        return self.__api._Api__call("operation_history", "get_transaction", [trx_id])
