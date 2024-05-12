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


class zuopin(models.Model):
    owner = models.ForeignKey(to='workman', on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default='')
    img = models.CharField(max_length=255, default='')
    size_type = models.IntegerField(default=0)


class interview(models.Model):
    owner = models.ForeignKey(to='workman', on_delete=models.CASCADE)
    interviewer = models.CharField(max_length=255, default='')
    translator = models.CharField(max_length=255, default='')
    time = models.CharField(max_length=255, default='')
    introduce = models.CharField(max_length=255, default='')
    question = models.TextField(default='')
    answer = models.TextField(default='')
    img = models.CharField(max_length=255, default='')