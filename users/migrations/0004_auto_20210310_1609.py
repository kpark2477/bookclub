# Generated by Django 2.2.5 on 2021-03-10 07:09

import core.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_bio'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', core.managers.CustomUserManager()),
            ],
        ),
    ]
