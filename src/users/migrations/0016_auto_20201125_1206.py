# Generated by Django 3.1.2 on 2020-11-25 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_remove_useraccount_picture'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useraccount',
            options={'ordering': ['user']},
        ),
    ]
