# Generated by Django 4.2.7 on 2023-11-21 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_alter_filesmodel_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filesmodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 21, 16, 58, 5, 582904)),
        ),
    ]