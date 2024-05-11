from django.db import models
import django.utils.timezone as timezone


class workman(models.Model):
    name = models.CharField(max_length=255, default='')
    ethic = models.CharField(max_length=255, default='')
    honor = models.TextField(max_length=255, default='')
    introduction = models.TextField(default='')
    birthday = models.DateField(default=timezone.now)
    img = models.CharField(max_length=255, default='')
    title = models.CharField(max_length=255, default='')
    koutu = models.CharField(max_length=255, default='')


class shop(models.Model):
    owner = models.ForeignKey(to='workman', on_delete=models.CASCADE)
    found_time = models.DateField(auto_now_add=True)
    range = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    contact = models.CharField(max_length=255, default='')
    img = models.CharField(max_length=255, default='')