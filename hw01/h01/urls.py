from django.conf.urls import url
from .views import checkList
urlpatterns=[
    url(r'^index',checkList)
]
