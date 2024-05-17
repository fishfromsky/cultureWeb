# Generated by Django 3.2.25 on 2024-05-12 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wqqweb', '0028_zuopin'),
    ]

    operations = [
        migrations.CreateModel(
            name='interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interviewer', models.CharField(default='', max_length=255)),
                ('translator', models.CharField(default='', max_length=255)),
                ('time', models.CharField(default='', max_length=255)),
                ('introduce', models.CharField(default='', max_length=255)),
                ('question', models.TextField(default='')),
                ('answer', models.TextField(default='')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wqqweb.workman')),
            ],
        ),
    ]