from django.db import models
from django.contrib.auth.models import AbstractUser
from .model_package.people import people_models
from .model_package.buy import buy_models
from .model_package.show import show_models


class UserProfile(AbstractUser):
    role = models.CharField(default='普通用户', max_length=10)
    token = models.CharField(max_length=255, verbose_name='token', default='')
    phone_number = models.CharField(max_length=255, default='')
    province = models.CharField(max_length=255, default='')
    district = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    sign = models.CharField(max_length=255, default='')
    post_price = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.username
