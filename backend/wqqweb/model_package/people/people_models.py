from django.db import models


class workman(models.Model):
    name = models.CharField(max_length=255, default='')
    ethic = models.CharField(max_length=255, default='')
    honor = models.CharField(max_length=255, default='')