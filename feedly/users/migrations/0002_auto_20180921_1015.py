# Generated by Django 2.1.1 on 2018-09-21 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myprofile',
            old_name='user',
            new_name='account',
        ),
    ]
