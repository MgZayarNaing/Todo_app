# Generated by Django 3.0 on 2023-11-21 00:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilesModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('file', models.FileField(default=None, upload_to='')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 11, 21, 7, 26, 34, 410270))),
            ],
        ),
    ]
