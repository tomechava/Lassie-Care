# Generated by Django 5.0.2 on 2024-05-20 23:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lassie', '0018_rename_food_dailytasks_food'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailytasks',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='dailytasks',
            name='water',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dailytasks',
            name='food',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dailytasks',
            name='walks',
            field=models.IntegerField(default=0),
        ),
    ]