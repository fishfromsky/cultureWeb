# Generated by Django 3.2.25 on 2024-04-26 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wqqweb', '0016_wen_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.TextField(default='')),
                ('type_id', models.IntegerField(default=0)),
                ('title', models.CharField(default='', max_length=255)),
                ('content', models.TextField(default='')),
            ],
        ),
    ]
