# Generated by Django 2.0.9 on 2020-03-16 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratu', '0002_auto_20200315_2209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
    ]