# Generated by Django 5.0.2 on 2024-05-20 23:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lassie', '0021_alter_dailytasks_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailytasks',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]