# Generated by Django 3.2.6 on 2022-02-15 17:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emadapp', '0002_alter_blogpost_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='post_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 15, 23, 35, 48, 809389)),
        ),
    ]
