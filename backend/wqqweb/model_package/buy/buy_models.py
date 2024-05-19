from django.db import models
from ..people.people_models import workman


class Categories(models.Model):
    name = models.CharField(max_length=255, default='')
    main_class = models.CharField(max_length=255, default='')


class Goods(models.Model):
    name = models.CharField(max_length=255, default='')
    price = models.FloatField(default=0)
    src = models.CharField(max_length=255, default='')
    person = models.ForeignKey(to='workman', on_delete=models.CASCADE)
    category = models.ForeignKey(to='Categories', null=True, on_delete=models.SET_NULL)


class GoodsInformation(models.Model):
    good_id = models.ForeignKey(to='Goods', on_delete=models.CASCADE)
    sizes = models.CharField(max_length=255, default='')
    child_list = models.TextField(default='')
    prices = models.CharField(max_length=255, default='')
    describe = models.TextField(default='')


class goodsComment(models.Model):
    goods_id = models.ForeignKey(to='Goods', on_delete=models.CASCADE)
    user = models.ForeignKey(to='UserProfile', on_delete=models.CASCADE)
    comment = models.TextField(default='')
    size = models.CharField(max_length=255, default='')

class Express_Addresses(models.Model):
    user = models.ForeignKey(to='UserProfile', on_delete=models.CASCADE)
    address = models.CharField(max_length=255, default='')


class buy_record(models.Model):
    goods = models.ForeignKey(to='Goods', on_delete=models.CASCADE)
    customer = models.ForeignKey(to='UserProfile', on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey(to='Express_Addresses', null=True, on_delete=models.SET_NULL)





