# Generated by Django 3.2.25 on 2024-04-01 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wqqweb', '0011_buy_record_express_addresses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show_Ji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('content', models.TextField(default='')),
                ('fig_title', models.CharField(default='', max_length=255)),
                ('fig_src', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
