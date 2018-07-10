class Tags:
    """
    Provides GOLOS tags api.
    """
    def __init__(self, api):
        self.__api = api

    @staticmethod
    def __check_types(limit: int,
                      select_authors: list = [],
                      select_tags: list = [],
                      filter_tags: list = [],
                      truncate_body: int = 0,
                      start_author: str = None,
                      start_permlink: str = None,
                      parent_author: str = None,
                      parent_permlink: str = None):
        if not isinstance(limit, int):
            raise TypeError("limit")
        if not isinstance(select_authors, list):
            raise TypeError("select_authors")
        if not isinstance(select_tags, list):
            raise TypeError("select_tags")
        if not isinstance(filter_tags, list):
            raise TypeError("filter_tags")
        if not isinstance(truncate_body, int):
            raise TypeError("truncate_body")
        if not isinstance(start_author, str):
            raise TypeError("start_author")
        if not isinstance(start_permlink, str):
            raise TypeError("start_permlink")
        if not isinstance(parent_author, str):
            raise TypeError("parent_author")
        if not isinstance(parent_permlink, str):
            raise TypeError("parent_permlink")

    def get_trending_tags(self,
                          start_tag: str, limit: int):
        """
        Returns the list of trending tags.
        :param start_tag: trending tag.
        :param limit: tags count in response.
        :return: List of trending tags.
        """
        if not isinstance(start_tag, str):
            raise TypeError("start_tag")
        if not isinstance(limit, int):
            raise TypeError("limit")
        if not 0 <= limit <= 100:
            raise ValueError("limit")
        return self.__api._Api__call("tags", "get_trending_tags", [start_tag, limit])

    def get_tags_used_by_author(self,
                                author: str):
        """
        Returns a list of tags used by an author.
        :param author: author name.
        :return: List of tags.
        """
        if not isinstance(author, str):
            raise TypeError("author")
        return self.__api._Api__call("tags", "get_tags_used_by_author", [author])

    def get_discussions_by_payout(self,
                                  limit: int,
                                  select_authors: list=[],
                                  select_tags: list=[],
                                  filter_tags: list = [],
                                  truncate_body: int=0,
                                  start_author: str=None,
                                  start_permlink: str=None,
                                  parent_author: str=None,
                                  parent_permlink: str=None):
        """
        Returns a list of discussions based on payout.
        :param limit: discussions count in response.
        :param select_authors: authors names.
        :param select_tags: tags list, discussions WITHOUT these tags will filtered.
        :param filter_tags: tags list, discussions WITH these tags will filtered.
        :param truncate_body: length in bytes of response body.
        :param start_author: author name to start with.
        :param start_permlink: permlink to start with.
        :param parent_author: author of parent discussion.
        :param parent_permlink: permlink of parent discussion.
        :return: List of discussions.
        """
        Tags.__check_types(limit, select_authors, select_tags, filter_tags, truncate_body,
                           start_author, start_permlink, parent_author, parent_permlink)
        return self.__api._Api__call("tags", "get_discussions_by_payout",
                                     [{"limit": limit,
                                       "select_authors": select_authors,
                                       "select_tags": select_tags,
                                       "filter_tags": filter_tags,
                                       "truncate_body": truncate_body,
                                       "start_author": start_author,
                                       "start_permlink": start_permlink,
                                       "parent_author": parent_author,
                                       "parent_permlink": parent_permlink}])

    def get_discussions_by_trending(self,
                                    limit: int,
                                    select_authors: list=[],
                                    select_tags: list=[],
                                    filter_tags: list = [],
                                    truncate_body: int=0,
                                    start_author: str=None,
                                    start_permlink: str=None,
                                    parent_author: str=None,
                                    parent_permlink: str=None):
        """
        Returns a list of discussions by trending.
        :param limit: discussions count in response.
        :param select_authors: authors names.
        :param select_tags: tags list, discussions WITHOUT these tags will filtered.
        :param filter_tags: tags list, discussions WITH these tags will filtered.
        :param truncate_body: length in bytes of response body.
        :param start_author: author name to start with.
        :param start_permlink: permlink to start with.
        :param parent_author: author of parent discussion.
        :param parent_permlink: permlink of parent discussion.
        :return: List of discussions.
        """
        Tags.__check_types(limit, select_authors, select_tags, filter_tags, truncate_body,
                           start_author, start_permlink, parent_author, parent_permlink)
        return self.__api._Api__call("tags", "get_discussions_by_trending",
                                     [{"limit": limit,
                                       "select_authors": select_authors,
                                       "select_tags": select_tags,
                                       "filter_tags": filter_tags,
                                       "truncate_body": truncate_body,
                                       "start_author": start_author,
                                       "start_permlink": start_permlink,
                                       "parent_author": parent_author,
                                       "parent_permlink": parent_permlink}])

    def get_discussions_by_created(self,
                                   limit: int,
                                   select_authors: list=[],
                                   select_tags: list=[],
                                   filter_tags: list = [],
                                   truncate_body: int=0,
                                   start_author: str=None,
                                   start_permlink: str=None,
                                   parent_author: str=None,
                                   parent_permlink: str=None):
        """
        Returns a list of discussions by created.
        :param limit: discussions count in response.
        :param select_authors: authors names.
        :param select_tags: tags list, discussions WITHOUT these tags will filtered.
        :param filter_tags: tags list, discussions WITH these tags will filtered.
        :param truncate_body: length in bytes of response body.
        :param start_author: author name to start with.
        :param start_permlink: permlink to start with.
        :param parent_author: author of parent discussion.
        :param parent_permlink: permlink of parent discussion.
        :return: List of discussions.
        """
        Tags.__check_types(limit, select_authors, select_tags, filter_tags, truncate_body,
                           start_author, start_permlink, parent_author, parent_permlink)
        return self.__api._Api__call("tags", "get_discussions_by_created",
                                     [{"limit": limit,
                                       "select_authors": select_authors,
                                       "select_tags": select_tags,
                                       "filter_tags": filter_tags,
                                       "truncate_body": truncate_body,
                                       "start_author": start_author,
                                       "start_permlink": start_permlink,
                                       "parent_author": parent_author,
                                       "parent_permlink": parent_permlink}])

    def get_discussions_by_cashout(self,
                                   limit: int,
                                   select_authors: list=[],
                                   select_tags: list=[],
                                   filter_tags: list = [],
                                   truncate_body: int=0,
                                   start_author: str=None,
                                   start_permlink: str=None,
                                   parent_author: str=None,
                                   parent_permlink: str=None):
        """
        Returns a list of discussions by cashout.
        :param limit: discussions count in response.
        :param select_authors: authors names.
        :param select_tags: tags list, discussions WITHOUT these tags will filtered.
        :param filter_tags: tags list, discussions WITH these tags will filtered.
        :param truncate_body: length in bytes of response body.
        :param start_author: author name to start with.
        :param start_permlink: permlink to start with.
        :param parent_author: author of parent discussion.
        :param parent_permlink: permlink of parent discussion.
        :return: List of discussions.
        """
        Tags.__check_types(limit, select_authors, select_tags, filter_tags, truncate_body,
                           start_author, start_permlink, parent_author, parent_permlink)
        return self.__api._Api__call("tags", "get_discussions_by_cashout",
                                     [{"limit": limit,
                                       "select_authors": select_authors,
                                       "select_tags": select_tags,
                                       "filter_tags": filter_tags,
                                       "truncate_body": truncate_body,
                                       "start_author": start_author,
                                       "start_permlink": start_permlink,
                                       "parent_author": parent_author,
                                       "parent_permlink": parent_permlink}])

    def get_discussions_by_votes(self,
                                 limit: int,
                                 select_authors: list=[],
                                 select_tags: list=[],
                                 filter_tags: list = [],
                                 truncate_body: int=0,
                                 start_author: str=None,
                                 start_permlink: str=None,
                                 parent_author: str=None,
                                 parent_permlink: str=None):
        """
        Returns a list of discussions by votes.
        :param limit: discussions count in response.
        :param select_authors: authors names.
        :param select_tags: tags list, discussions WITHOUT these tags will filtered.
        :param filter_tags: tags list, discussions WITH these tags will filtered.
        :param truncate_body: length in bytes of response body.
        :param start_author: author name to start with.
        :param start_permlink: permlink to start with.
        :param parent_author: author of parent discussion.
        :param parent_permlink: permlink of parent discussion.
        :return: List of discussions.
        """
        Tags.__check_types(limit, select_authors, select_tags, filter_tags, truncate_body,
                           start_author, start_permlink, parent_author, parent_permlink)
        return self.__api._Api__call("tags", "get_discussions_by_votes",
                                     [{"limit": limit,
                                       "select_authors": select_authors,
                                       "select_tags": select_tags,
                                       "filter_tags": filter_tags,
                                       "truncate_body": truncate_body,
                                       "start_author": start_author,
                                       "start_permlink": start_permlink,
                                       "parent_author": parent_author,
                                       "parent_permlink": parent_permlink}])

    def get_discussions_by_children(self,
                                    limit: int,
                                    select_authors: list=[],
                                    select_tags: list=[],
                                    filter_tags: list = [],
                                    truncate_body: int=0,
                                    start_author: str=None,
                                    start_permlink: str=None,
                                    parent_author: str=None,
                                    parent_permlink: str=None):
        """
        Returns a list of discussions by children.
        :param limit: discussions count in response.
        :param select_authors: authors names.
        :param select_tags: tags list, discussions WITHOUT these tags will filtered.
        :param filter_tags: tags list, discussions WITH these tags will filtered.
        :param truncate_body: length in bytes of response body.
        :param start_author: author name to start with.
        :param start_permlink: permlink to start with.
        :param parent_author: author of parent discussion.
        :param parent_permlink: permlink of parent discussion.
        :return: List of discussions.
        """
        Tags.__check_types(limit, select_authors, select_tags, filter_tags, truncate_body,
                           start_author, start_permlink, parent_author, parent_permlink)
        return self.__api._Api__call("tags", "get_discussions_by_children",
                                     [{"limit": limit,
                                       "select_authors": select_authors,
                                       "select_tags": select_tags,
                                       "filter_tags": filter_tags,
                                       "truncate_body": truncate_body,
                                       "start_author": start_author,
                                       "start_permlink": start_permlink,
                                       "parent_author": parent_author,
                                       "parent_permlink": parent_permlink}])

    def get_discussions_by_hot(self,
                               limit: int,
                               select_authors: list=[],
                               select_tags: list=[],
                               filter_tags: list = [],
                               truncate_body: int=0,
                               start_author: str=None,
                               start_permlink: str=None,
                               parent_author: str=None,
                               parent_permlink: str=None):
        """
        Returns a list of discussions by hot.
        :param limit: discussions count in response.
        :param select_authors: authors names.
        :param select_tags: tags list, discussions WITHOUT these tags will filtered.
        :param filter_tags: tags list, discussions WITH these tags will filtered.
        :param truncate_body: length in bytes of response body.
        :param start_author: author name to start with.
        :param start_permlink: permlink to start with.
        :param parent_author: author of parent discussion.
        :param parent_permlink: permlink of parent discussion.
        :return: List of discussions.
        """
        Tags.__check_types(limit, select_authors, select_tags, filter_tags, truncate_body,
                           start_author, start_permlink, parent_author, parent_permlink)
        return self.__api._Api__call("tags", "get_discussions_by_hot",
                                     [{"limit": limit,
                                       "select_authors": select_authors,
                                       "select_tags": select_tags,
                                       "filter_tags": filter_tags,
                                       "truncate_body": truncate_body,
                                       "start_author": start_author,
                                       "start_permlink": start_permlink,
                                       "parent_author": parent_author,
                                       "parent_permlink": parent_permlink}])

    def get_discussions_by_feed(self,
                                limit: int,
                                select_authors: list=[],
                                select_tags: list=[],
                                filter_tags: list = [],
                                truncate_body: int=0,
                                start_author: str=None,
                                start_permlink: str=None,
                                parent_author: str=None,
                                parent_permlink: str=None):
        """
        Returns a list of discussions by feed.
        :param limit: discussions count in response.
        :param select_authors: authors names.
        :param select_tags: tags list, discussions WITHOUT these tags will filtered.
        :param filter_tags: tags list, discussions WITH these tags will filtered.
        :param truncate_body: length in bytes of response body.
        :param start_author: author name to start with.
        :param start_permlink: permlink to start with.
        :param parent_author: author of parent discussion.
        :param parent_permlink: permlink of parent discussion.
        :return: List of discussions.
        """
        Tags.__check_types(limit, select_authors, select_tags, filter_tags, truncate_body,
                           start_author, start_permlink, parent_author, parent_permlink)
        return self.__api._Api__call("tags", "get_discussions_by_feed",
                                     [{"limit": limit,
                                       "select_authors": select_authors,
                                       "select_tags": select_tags,
                                       "filter_tags": filter_tags,
                                       "truncate_body": truncate_body,
                                       "start_author": start_author,
                                       "start_permlink": start_permlink,
                                       "parent_author": parent_author,
                                       "parent_permlink": parent_permlink}])

    def get_discussions_by_blog(self,
                                limit: int,
                                select_authors: list = [],
                                select_tags: list = [],
                                filter_tags: list = [],
                                truncate_body: int = 0,
                                start_author: str = None,
                                start_permlink: str = None,
                                parent_author: str = None,
                                parent_permlink: str = None):
        """
        Returns a list of discussions by blog.
        :param limit: discussions count in response.
        :param select_authors: authors names.
        :param select_tags: tags list, discussions WITHOUT these tags will filtered.
        :param filter_tags: tags list, discussions WITH these tags will filtered.
        :param truncate_body: length in bytes of response body.
        :param start_author: author name to start with.
        :param start_permlink: permlink to start with.
        :param parent_author: author of parent discussion.
        :param parent_permlink: permlink of parent discussion.
        :return: List of discussions.
        """
        Tags.__check_types(limit, select_authors, select_tags, filter_tags, truncate_body,
                           start_author, start_permlink, parent_author, parent_permlink)
        return self.__api._Api__call("tags", "get_discussions_by_blog",
                                     [{"limit": limit,
                                       "select_authors": select_authors,
                                       "select_tags": select_tags,
                                       "filter_tags": filter_tags,
                                       "truncate_body": truncate_body,
                                       "start_author": start_author,
                                       "start_permlink": start_permlink,
                                       "parent_author": parent_author,
                                       "parent_permlink": parent_permlink}])

    def get_discussions_by_comments(self,
                                    start_author: str,
                                    limit: int,
                                    select_authors: list = [],
                                    select_tags: list = [],
                                    filter_tags: list = [],
                                    truncate_body: int = 0,
                                    start_permlink: str = None,
                                    parent_author: str = None,
                                    parent_permlink: str = None):
        """
        Returns a list of discussions by comments.
        :param limit: discussions count in response.
        :param select_authors: authors names.
        :param select_tags: tags list, discussions WITHOUT these tags will filtered.
        :param filter_tags: tags list, discussions WITH these tags will filtered.
        :param truncate_body: length in bytes of response body.
        :param start_author: author name to start with.
        :param start_permlink: permlink to start with.
        :param parent_author: author of parent discussion.
        :param parent_permlink: permlink of parent discussion.
        :return: List of discussions.
        """
        Tags.__check_types(limit, select_authors, select_tags, filter_tags, truncate_body,
                           start_author, start_permlink, parent_author, parent_permlink)
        return self.__api._Api__call("tags", "get_discussions_by_comments",
                                     [{"limit": limit,
                                       "select_authors": select_authors,
                                       "select_tags": select_tags,
                                       "filter_tags": filter_tags,
                                       "truncate_body": truncate_body,
                                       "start_author": start_author,
                                       "start_permlink": start_permlink,
                                       "parent_author": parent_author,
                                       "parent_permlink": parent_permlink}])

    def get_discussions_by_promoted(self,
                                    limit: int,
                                    select_authors: list = [],
                                    select_tags: list = [],
                                    filter_tags: list = [],
                                    truncate_body: int = 0,
                                    start_author: str = None,
                                    start_permlink: str = None,
                                    parent_author: str = None,
                                    parent_permlink: str = None):
        """
        Returns a list of discussions by promoted.
        :param limit: discussions count in response.
        :param select_authors: authors names.
        :param select_tags: tags list, discussions WITHOUT these tags will filtered.
        :param filter_tags: tags list, discussions WITH these tags will filtered.
        :param truncate_body: length in bytes of response body.
        :param start_author: author name to start with.
        :param start_permlink: permlink to start with.
        :param parent_author: author of parent discussion.
        :param parent_permlink: permlink of parent discussion.
        :return: List of discussions.
        """
        Tags.__check_types(limit, select_authors, select_tags, filter_tags, truncate_body,
                           start_author, start_permlink, parent_author, parent_permlink)
        return self.__api._Api__call("tags", "get_discussions_by_promoted",
                                     [{"limit": limit,
                                       "select_authors": select_authors,
                                       "select_tags": select_tags,
                                       "filter_tags": filter_tags,
                                       "truncate_body": truncate_body,
                                       "start_author": start_author,
                                       "start_permlink": start_permlink,
                                       "parent_author": parent_author,
                                       "parent_permlink": parent_permlink}])

    def get_discussions_by_author_before_date(self,
                                              author: str, start_permlink: str,
                                              before_date: str, limit: int):
        """
        Returns a list of discussions based on author before date.
        :param author: author name.
        :param start_permlink: permlink to start with.
        :param before_date: ISO 8601 formatted date and time
        :param limit: discussions count in response.
        :return: List of discussions.
        """
        if not isinstance(author, str):
            raise TypeError("author")
        if not isinstance(start_permlink, str):
            raise TypeError("start_permlink")
        if not isinstance(before_date, str):
            raise TypeError("before_date")
        if not isinstance(limit, int):
            raise TypeError("limit")
        if not 1 <= limit <= 100:
            raise ValueError("limit")
        return self.__api._Api__call("tags", "get_discussions_by_author_before_date",
                                     [author, start_permlink, before_date, limit])

    def get_languages(self):
        """
        Returns a languages.
        :return: List of languages.
        """
        return self.__api._Api__call("tags", "get_languages", [])
