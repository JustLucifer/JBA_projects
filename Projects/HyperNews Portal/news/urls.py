from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', soon, name='news'),
    path('news/', index_view, name='news'),
    path('news/create/', create_post, name='create_post'),
    re_path("news/(?P<post_id>[^/]*)/?/", show_post, name='show_post'),
]
