# Generated by Django 4.2.3 on 2023-07-27 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_useraddressinformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=300)),
            ],
        ),
    ]
