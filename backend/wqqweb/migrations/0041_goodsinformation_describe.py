# Generated by Django 3.2.25 on 2024-05-19 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wqqweb', '0040_userprofile_post_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsinformation',
            name='describe',
            field=models.TextField(default=''),
        ),
    ]