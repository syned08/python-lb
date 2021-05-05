from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('post/<int:post_id>', go_link, name="go_link"),
]