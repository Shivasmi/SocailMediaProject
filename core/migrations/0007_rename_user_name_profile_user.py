# Generated by Django 4.2.3 on 2023-07-30 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_user_profile_user_name_repost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_name',
            new_name='user',
        ),
    ]