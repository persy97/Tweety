from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from django.db.models import Q
from .secretkeys import *
import json
import time
from rest_framework import generics
from .serializers import TweetSerializer
from .models import *


class StdOutListener(StreamListener):
    def __init__(self, time_limit=10):
        self.start_time = time.time()
        self.limit = time_limit
        super(StdOutListener, self).__init__()

    def on_data(self, data):
        if (time.time() - self.start_time) > self.limit:
            return False
        d = json.loads(data)
        a = Modell(status=d['text'], username=d['user']['name'], location=d['user']['location'],
                   retweet_count=d['retweet_count'], reply_count=d['reply_count'], favorite_count=d['favorite_count'])
        a.save()

        for i in d['entities']['user_mentions']:
            r = UserMentions(tweet =a, useridname=i['name'])
            r.save()
        for i in d['entities']['hashtags']:
            r = Hashtags(tweetidd=a, hashtag=i['text'])
            r.save()
        return True

    def on_error(self, status):
        print(status)
        return False


class TweetList(generics.ListAPIView):
    serializer_class = TweetSerializer

    def get_queryset(self):
        l = StdOutListener()
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(akey, asecret)
        stream = Stream(auth, l)
        stream.filter(track=[self.request.GET.get('filter')])
        queryset = Modell.objects.all()
        if self.request.GET.get('location'):
            queryset = queryset.filter(location__contains=self.request.GET.get('location'))
        return queryset