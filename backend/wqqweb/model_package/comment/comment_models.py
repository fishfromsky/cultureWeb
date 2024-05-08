from django.db import models


class Comment(models.Model):
    content = models.CharField(max_length=255, default='')
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to='UserProfile', on_delete=models.CASCADE)


class Liking(models.Model):
    comment = models.ForeignKey(to='Comment', null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(to='UserProfile', on_delete=models.CASCADE)


class Guanzhu(models.Model):
    user = models.ForeignKey(to='UserProfile', on_delete=models.CASCADE)
    target_user = models.ForeignKey(to='UserProfile', on_delete=models.CASCADE, related_name='target_user')


class Shoucang(models.Model):
    user = models.ForeignKey(to='UserProfile', on_delete=models.CASCADE)
    comment = models.ForeignKey(to='Comment', null=True, on_delete=models.SET_NULL)


class Pinglun(models.Model):
    user = models.ForeignKey(to='UserProfile', on_delete=models.CASCADE)
    comment = models.ForeignKey(to='Comment', null=True, on_delete=models.SET_NULL)
    content = models.CharField(max_length=255, default='')