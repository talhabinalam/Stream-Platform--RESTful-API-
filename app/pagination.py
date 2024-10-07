from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class WatchListPGPagination(PageNumberPagination):
    page_size = 3
    # page_query_param = 'p'

    # User Side Customizaton
    page_size_query_param = 'size'
    max_page_size = 10  #restrict user to load this maximum elements

    # last_page_strings = 'ends'

class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 5

    max_limit = 10

    limit_query_param = 'limit'
    offset_query_param = 'starts'

class WatchListCUPagination(CursorPagination):
    page_size = 5
    ordering = 'created'
    cursor_query_param = 'record'