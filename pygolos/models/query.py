class Query:
    def __init__(self,
                 limit: int,
                 select_authors: list=None,
                 select_tags: list=None,
                 filter_tags: list=None,
                 truncate_body: int=None,
                 start_author: str=None,
                 start_permlink: str=None,
                 parent_author: str=None,
                 parent_permlink: str=None):
        self.limit = limit
        self.select_authors = select_authors
        self.select_tags = select_tags
        self.filter_tags = filter_tags
        self.truncate_body = truncate_body
        self.start_author = start_author
        self.start_permlink = start_permlink
        self.parent_author = parent_author
        self.parent_permlink = parent_permlink

    def jsonify(self):
        from json import dumps
        return dumps(dict((k, v) for k, v in self.__dict__.items() if v is not None))
