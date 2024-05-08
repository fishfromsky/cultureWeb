from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, default='')
    content = models.TextField(default='')
    category = models.IntegerField(default=0)
    sub_title = models.CharField(max_length=100, default='')
    news_time = models.DateField(auto_now_add=True)