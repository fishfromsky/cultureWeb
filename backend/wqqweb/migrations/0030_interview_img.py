# Generated by Django 3.2.25 on 2024-05-12 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wqqweb', '0029_interview'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='img',
            field=models.CharField(default='', max_length=255),
        ),
    ]
