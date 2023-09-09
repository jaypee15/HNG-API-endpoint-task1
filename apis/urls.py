from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GetInfo

urlpatterns = [
    path("api/", GetInfo.as_view(), name="api"),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])