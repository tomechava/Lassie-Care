# Generated by Django 5.0.2 on 2024-05-20 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lassie', '0017_dailytasks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailytasks',
            old_name='Food',
            new_name='food',
        ),
    ]