from django.urls import re_path
from .views import Register

urlpatterns = [
    re_path(r'^api/register/$' , Register.as_view(), name='register')
]