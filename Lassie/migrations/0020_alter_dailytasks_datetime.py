# Generated by Django 5.0.2 on 2024-05-20 23:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lassie', '0019_dailytasks_datetime_dailytasks_water_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailytasks',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 20, 23, 9, 47, 575203, tzinfo=datetime.timezone.utc)),
        ),
    ]