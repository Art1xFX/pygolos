class NetworkBroadcastApi:
    """
    Provides GOLOS network_broadcast_api classes.
    """
    def __init__(self, api):
        self.__api = api

    def broadcast_transaction(self,
                              ref_block_num: int,
                              ref_block_prefix,
                              expiration: str,
                              operations: list,
                              extensions: list,
                              signatures: list):
        """
        Used to broadcast a transaction.
        :param ref_block_num: number of the previous block.
        :param ref_block_prefix: last 4 bytes of block id.
        :param expiration: expiration time of transaction.
        :param operations: operations in block.
        :param signatures: signatures of block.
        :return:
        """
        return self.__api._Api__call("network_broadcast_api", "broadcast_transaction",
                                     [{"trx": {
                                         "ref_block_num": ref_block_num,
                                         "ref_block_prefix": ref_block_prefix,
                                         "expiration": expiration,
                                         "operations": operations,
                                         "extensions": extensions,
                                         "signatures": signatures}}])

    def broadcast_transaction_with_callback(self,
                                            confirmation_callback,
                                            ref_block_num: int,
                                            ref_block_prefix,
                                            expiration: str,
                                            operations: list,
                                            extensions: list,
                                            signatures: list):
        """
        Used to broadcast a transaction.
        :param ref_block_num: number of the previous block.
        :param ref_block_prefix: last 4 bytes of block id.
        :param expiration: expiration time of transaction.
        :param operations: operations in block.
        :param signatures: signatures of block.
        :return:
        """
        return self.__api._Api__call("network_broadcast_api", "broadcast_transaction_with_callback",
                                     [confirmation_callback, {"trx": {
                                         "ref_block_num": ref_block_num,
                                         "ref_block_prefix": ref_block_prefix,
                                         "expiration": expiration,
                                         "operations": operations,
                                         "extensions": extensions,
                                         "signatures": signatures}}])

    def broadcast_transaction_synchronous(self,
                                          ref_block_num: int,
                                          ref_block_prefix,
                                          expiration: str,
                                          operations: list,
                                          extensions: list,
                                          signatures: list):
        """
        Used to broadcast a transaction and waits for it to be processed synchronously.
        :param ref_block_num: number of the previous block.
        :param ref_block_prefix: last 4 bytes of block id.
        :param expiration: expiration time of transaction.
        :param operations: operations in block.
        :param signatures: signatures of block.
        :return:
        """
        return self.__api._Api__call("network_broadcast_api", "broadcast_transaction_synchronous",
                                     [{"trx": {
                                         "ref_block_num": ref_block_num,
                                         "ref_block_prefix": ref_block_prefix,
                                         "expiration": expiration,
                                         "operations": operations,
                                         "extensions": extensions,
                                         "signatures": signatures}}])

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

    def broadcast_transaction_synchronous2(self,
                                          trx):
        """
        Used to broadcast a transaction and waits for it to be processed synchronously.
        :param ref_block_num: number of the previous block.
        :param ref_block_prefix: last 4 bytes of block id.
        :param expiration: expiration time of transaction.
        :param operations: operations in block.
        :param signatures: signatures of block.
        :return:
        """
        from json import loads
        return self.__api._Api__call("network_broadcast_api", "broadcast_transaction_synchronous",
                                     [loads(trx.jsonify())])
