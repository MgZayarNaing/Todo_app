# Generated by Django 3.0 on 2023-11-21 00:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filesmodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 21, 7, 27, 16, 328176)),
        ),
    ]
