# Generated by Django 2.1.2 on 2018-11-03 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginlogout', '0003_users_token'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
