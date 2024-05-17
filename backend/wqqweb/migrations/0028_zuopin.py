# Generated by Django 3.2.25 on 2024-05-12 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wqqweb', '0027_shop_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='zuopin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='', max_length=255)),
                ('img', models.CharField(default='', max_length=255)),
                ('size_type', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wqqweb.workman')),
            ],
        ),
    ]