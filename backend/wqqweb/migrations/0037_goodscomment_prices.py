# Generated by Django 3.2.25 on 2024-05-18 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wqqweb', '0036_goodscomment_goodsinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodscomment',
            name='prices',
            field=models.CharField(default='', max_length=255),
        ),
    ]