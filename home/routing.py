from django.urls import path, re_path

from home.consumers import *

ws_patterns = [re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatConsumer.as_asgi())]
