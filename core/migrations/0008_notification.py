# Generated by Django 4.2.3 on 2023-08-04 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_user_name_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likepost', models.CharField(max_length=100)),
                ('likeby', models.ManyToManyField(to='core.post')),
            ],
        ),
    ]
