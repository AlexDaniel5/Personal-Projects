# Generated by Django 5.0.1 on 2024-01-17 03:42

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='voteToSkip',
            new_name='votesToSkip',
        ),
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default=api.models.generateUniqueCode, max_length=8, unique=True),
        ),
    ]
