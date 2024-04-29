# Generated by Django 5.0.2 on 2024-04-29 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lassie', '0006_rename_adress_ownerprofile_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='petprofile',
            old_name='Weight',
            new_name='weight',
        ),
        migrations.RemoveField(
            model_name='petprofile',
            name='files',
        ),
        migrations.AddField(
            model_name='petprofile',
            name='breed',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Lassie.dogbreed'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='petprofile',
            name='medicalHistory',
            field=models.FileField(blank=True, null=True, upload_to='media/medical_history'),
        ),
    ]