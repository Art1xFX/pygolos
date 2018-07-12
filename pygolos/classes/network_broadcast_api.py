class NetworkBroadcastApi:
    """
    Provides GOLOS network_broadcast_api classes.
    """
    def __init__(self, api):
        self.__api = api

    def broadcast_transaction(self,
                              transaction):
        """
        Used to broadcast a transaction.
        :param transaction: transaction to broadcast.
        :return:
        """
        return self.__api._Api__call("network_broadcast_api", "broadcast_transaction",
                                     [transaction])

    def broadcast_transaction_with_callback(self,
                                            transaction):
        """
        Used to broadcast a transaction.
        :param transaction: transaction to broadcast.
        :return:
        """
        return self.__api._Api__call("network_broadcast_api", "broadcast_transaction_with_callback",
                                     [transaction])

    def broadcast_transaction_synchronous(self,
                                          transaction):
        """
        Used to broadcast a transaction and waits for it to be processed synchronously.
        :param transaction: transaction to broadcast.
        :return:
        """
        return self.__api._Api__call("network_broadcast_api", "broadcast_transaction_synchronous",
                                     [transaction])

    def broadcast_block(self,
                        previous: str,
                        timestamp: str,
                        witness: str,
                        transaction_merkle_root: str,
                        extensions: list,
                        witness_signature: str,
                        transactions: list):
        return self.__api._Api__call("network_broadcast_api", "broadcast_transaction_synchronous",
                                     [{"previous": previous,
                                       "timestamp": timestamp,
                                       "witness": witness,
                                       "transaction_merkle_root": transaction_merkle_root,
                                       "extensions": extensions,
                                       "witness_signature": witness_signature,
                                       "transactions": transactions}])
