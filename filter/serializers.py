from rest_framework import serializers
from .models import UserMentions, Hashtags, Modell


class UserMentionSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserMentions
        fields = ('useridname','tweet')


class HashtagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hashtags
        fields = ('tweetidd', 'hashtag')


class TweetSerializer(serializers.ModelSerializer):
    MentionedUsers = UserMentionSerializer(source='getUserMention', many=True)
    HashtagList = HashtagsSerializer(source='gethashtag', many=True)

    class Meta:
        model = Modell
        fields = ('status', 'username', 'location', 'retweet_count', 'reply_count', 'favorite_count', 'MentionedUsers',
                  'HashtagList')

