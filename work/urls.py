from django.urls import re_path
from .views import Register

urlpatterns = [
    re_path(r'^/api/works/$' , Works.as_view(), name='Works'),
    re_path(r'^/api/works/(?P<artist>\w{0,50})/$' , Works.as_view(), name='Works'),
    re_path(r'^/api/works/(?P<work_type>\w{0,50})/$' , Works.as_view(), name='Works')
]

