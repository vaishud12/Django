from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import UserRateThrottle
class StandardResultsSetPagination(PageNumberPagination):
    page_size=2 #by default page size
    max_page_size=1600 #max page size
    page_size_query_param='page_size' #dynamic page size
class CustomThrottle(UserRateThrottle):
    rate='3/hour'