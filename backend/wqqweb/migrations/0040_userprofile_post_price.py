# Generated by Django 3.2.25 on 2024-05-19 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wqqweb', '0039_auto_20240518_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='post_price',
            field=models.CharField(default='', max_length=255),
        ),
    ]