from rest_framework.pagination import PageNumberPagination


class ModulePaginator(PageNumberPagination):
    page_size = 4
