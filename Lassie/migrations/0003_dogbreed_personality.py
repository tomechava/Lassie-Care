# Generated by Django 5.0.2 on 2024-04-15 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lassie', '0002_ownerprofile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogbreed',
            name='personality',
            field=models.JSONField(default=' '),
        ),
    ]