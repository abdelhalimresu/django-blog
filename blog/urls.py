from django.urls import path
from blog.views import add_post

urlpatterns = [
    path('post/add', add_post)
]