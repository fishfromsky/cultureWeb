# Generated by Django 3.2.25 on 2024-05-14 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wqqweb', '0033_history_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='type_id',
            field=models.IntegerField(default=0, max_length=255),
        ),
    ]
