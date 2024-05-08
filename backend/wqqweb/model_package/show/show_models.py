from django.db import models


class Show_Ji(models.Model):
    title = models.CharField(max_length=255, default='')
    content = models.TextField(default='')
    fig_title = models.CharField(max_length=255, default='')
    fig_src = models.CharField(max_length=255, default='')


class Show_Wen(models.Model):
    title = models.CharField(max_length=255, default='')
    content = models.TextField(default='')
    type_id = models.IntegerField(default=0)


class Wen_Table(models.Model):
    category = models.ForeignKey(to="Show_Wen", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='')
    content = models.TextField(default='')
    src = models.CharField(max_length=255, default='')
    vice_src = models.CharField(max_length=255, default='')


class Wen_Comment(models.Model):
    user = models.ForeignKey(to='UserProfile', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, default='')
    wen = models.ForeignKey(to='Wen_Table', on_delete=models.CASCADE)


class Material_Detail(models.Model):
    img = models.TextField(default='')
    type_id = models.IntegerField(default=0)
    title = models.CharField(max_length=255, default='')
    content = models.TextField(default='')