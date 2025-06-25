from django.urls import re_path
from .consumers import ChatConsumer

ws_urlpatterns = [
    re_path(r'^ws/group/(?P<group_pk>\d+)/$', ChatConsumer.as_asgi()),
]