from django.urls import path
from .views import TweetList

urlpatterns = [
    path('filter', TweetList.as_view(), name='home'),
]