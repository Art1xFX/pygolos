import json


class FollowApi:
    def __init__(self, api):
        self.__api = api

    def get_followers(self,following:str, startFollower:str, followType:str, limit:int):
        """

        Returns the list of followers for an account.
        :param following: Username string
        :param startFollower: username string
        :param followType: {undefined,blog,ignore}
        :param limit:>0
        :return:
        """
        if limit<0 or limit>1000:
            raise TypeError
        return self.__api._Api__call("follow","get_followers",[following,startFollower,followType,limit])

    def get_following(self,following:str, startFollower:str, followType:str, limit:int):
        """
        Returns the list of accounts that are following an account.
        :param following: Username string
        :param startFollower: username string
        :param followType: {undefined,blog,ignore}
        :param limit:>0
        """
        if limit<0 or limit>1000:
            raise TypeError
        return self.__api._Api__call("follow","get_following",[following,startFollower,followType,limit])

    def get_follow_count(self,account:str):
        """
        Returns the count of followers for an account.
        :param account: Account name (string)
        """
        return self.__api._Api__call("follow","get_follow_count",[account])

    def get_feed_entries(self,account:str,entryId:int,limit:int):
        """
        Returns a list of entries in an account’s feed.
        :param account:string
        :param entryId:int
        :param limit:int
        """
        if limit<0 or limit>500:
            raise TypeError
        return self.__api._Api__call("follow","get_feed_entries",[account,entryId,limit])

    def get_feed(self,account:str,entryId:int,limit:int):
        """
        Returns a list of items in an account’s feed
        :param account:string
        :param entryId:int
        :param limit:int
        """
        if limit<0 or limit>500:
            raise TypeError
        return self.__api._Api__call("follow","get_feed",[account,entryId,limit])

    def get_blog_entries(self,account:str,entryId:int,limit:int):
        """
        Returns a list of entries in an account’s feed.
        :param account:string
        :param entryId:int
        :param limit:int
        """
        if limit<0 or limit>500:
            raise TypeError
        return self.__api._Api__call("follow","get_blog_entries",[account,entryId,limit])

    def get_blog(self,account:str,entryId:int,limit:int):
        """
        Returns a list of blog entries for an account.
        :param account:string
        :param entryId:int
        :param limit:int
        """
        if limit<0 or limit>500:
            raise TypeError
        return self.__api._Api__call("follow","get_blog",[account,entryId,limit])


    def get_account_reputations(self,names:list):
        """
        Returns a list of account reputations.
        :param names: List type
        :return:
        """
        return self.__api._Api__call("follow","get_account_reputations",[names])

    def get_reblogged_by(self,author:str,permalink:str):
        """
        Returns a list of authors that have reblogged a post.
        :param author:string
        :param permalink:string
        :return:
        """
        return self.__api._Api__call("follow","get_reblogged_by",[author,permalink])

    def get_blog_authors(self,blogAccount:str):
        """
        Returns a list of authors that have had their content reblogged on a given blog account.
        :param blogAccount:string
        :return:
        """
        return self.__api._Api__call("follow","get_blog_authors",[blogAccount])