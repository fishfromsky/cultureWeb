# Generated by Django 3.2.25 on 2024-05-18 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wqqweb', '0037_goodscomment_prices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodsinformation',
            name='comment',
        ),
    ]