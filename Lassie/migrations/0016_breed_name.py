# Generated by Django 5.0.2 on 2024-05-16 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lassie', '0015_breed_alter_petprofile_breed'),
    ]

    operations = [
        migrations.AddField(
            model_name='breed',
            name='name',
            field=models.CharField(default='Breed', max_length=100),
        ),
    ]
