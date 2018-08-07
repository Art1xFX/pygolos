import json

class CollectionApi:
    def __init__(self, api):
        self.__api = api

    def get_collection(self, permlink: str):
        return self.__api._Api__call("collection_api", "get_collection", [permlink])

    def get_collection_marks(self, permlink: str):
        return self.__api._Api__call("collection_api", "get_collection_marks", [permlink])
