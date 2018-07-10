class SocialNetwork:
    """
    Provides GOLOS social_network api.
    """
    def __init__(self, api):
        self.__api = api

    def get_replies_by_last_update(self,
                                   start_parent_author: str, start_permlink: str, limit: int, vote_limit: int):
        """
        Returns a list of replies by last update.
        :param start_parent_author: parent authors of reply name.
        :param start_permlink: permlink to start with.
        :param limit: count of replies in response.
        :param vote_limit: limit of votes.
        :return: List of replies.
        """
        if not isinstance(start_parent_author, str):
            raise TypeError("start_parent_author")
        if not isinstance(start_permlink, str):
            raise TypeError("start_permlink")
        if not isinstance(limit, int):
            raise TypeError("limit")
        if not isinstance(vote_limit, int):
            raise TypeError("vote_limit")
        if not 1 <= limit <= 100:
            raise ValueError("limit")
        return self.__api._Api__call("social_network", "get_replies_by_last_update",
                                     [start_parent_author, start_permlink, limit, vote_limit])

    def get_content(self,
                    author: str, permlink: str, vote_limit: int):
        """
        Returns the content (post or comment).
        :param author: parent authors of reply name.
        :param permlink: permlink of post or comment.
        :param vote_limit: limit of votes.
        :return: Content.
        """
        if not isinstance(author, str):
            raise TypeError("author")
        if not isinstance(permlink, str):
            raise TypeError("permlink")
        if not isinstance(vote_limit, int):
            raise TypeError("vote_limit")
        return self.__api._Api__call("social_network", "get_content",
                                     [author, permlink, vote_limit])

    def get_content_replies(self,
                            parent: str, parent_permlink: str, vote_limit: int):
        """
        Returns a list of replies to post or comment.
        :param parent: parent authors of reply name.
        :param parent_permlink: permlink of parent post or comment.
        :param vote_limit: limit of votes.
        :return: List of replies. .
        """
        if not isinstance(parent, str):
            raise TypeError("parent")
        if not isinstance(parent_permlink, str):
            raise TypeError("parent_permlink")
        if not isinstance(vote_limit, int):
            raise TypeError("vote_limit")
        return self.__api._Api__call("social_network", "get_content_replies",
                                     [parent, parent_permlink, vote_limit])

    def get_all_content_replies(self,
                                parent: str, parent_permlink: str, vote_limit: int):
        """
        Returns a list of all replies to post or comment.
        :param parent: parent authors of reply name.
        :param parent_permlink: permlink of parent post or comment.
        :param vote_limit: limit of votes.
        :return: List of replies.
        """
        if not isinstance(parent, str):
            raise TypeError("parent")
        if not isinstance(parent_permlink, str):
            raise TypeError("parent_permlink")
        if not isinstance(vote_limit, int):
            raise TypeError("vote_limit")
        return self.__api._Api__call("social_network", "get_all_content_replies",
                                     [parent, parent_permlink, vote_limit])

    def get_active_votes(self,
                         author: str, permlink: str, vote_limit: int):
        """
        Returns all votes for the given post.
        :param author: parent authors of reply name.
        :param permlink: permlink of post or comment.
        :param vote_limit: limit of votes.
        :return: Content.
        """
        if not isinstance(author, str):
            raise TypeError("author")
        if not isinstance(permlink, str):
            raise TypeError("permlink")
        if not isinstance(vote_limit, int):
            raise TypeError("vote_limit")
        return self.__api._Api__call("social_network", "get_active_votes",
                                     [author, permlink, vote_limit])

    def get_account_votes(self,
                          author: str, start: int, vote_limit: int):
        """
        Returns all votes by an account.
        :param author: authors of reply name.
        :param start: start date.
        :param vote_limit: limit of votes.
        :return: Content.
        """
        if not isinstance(author, str):
            raise TypeError("author")
        if not isinstance(start, int):
            raise TypeError("start")
        if not isinstance(vote_limit, int):
            raise TypeError("vote_limit")
        return self.__api._Api__call("social_network", "get_account_votes",
                                     [author, start, vote_limit])
