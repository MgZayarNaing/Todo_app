# Generated by Django 3.0 on 2023-11-21 01:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_auto_20231121_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filesmodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 21, 7, 37, 43, 568135)),
        ),
    ]
