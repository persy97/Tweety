from django.db import models


class Modell(models.Model):
    status = models.CharField(max_length=4000)
    username = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=1000,  blank=True, null=True, default=' ')
    retweet_count = models.IntegerField(default=0)
    reply_count = models.IntegerField(default=0)
    favorite_count = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class UserMentions(models.Model):
    tweet = models.ForeignKey(Modell,  on_delete=models.CASCADE, related_name='getUserMention')
    useridname = models.CharField(max_length=100)

    def __str__(self):
        return self.useridname


class Hashtags(models.Model):
    tweetidd = models.ForeignKey(Modell, on_delete=models.CASCADE, related_name='gethashtag')
    hashtag = models.CharField(max_length=100)

    def __str__(self):
        return "#"+self.hashtag