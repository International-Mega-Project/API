from django.urls import path
from . import views

urlpatterns = [
    path('/api/postdata', views.index, name="post_data"),
    path('/api/getdata', views.index, name="get_data"),
]
