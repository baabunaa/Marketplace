# Generated by Django 3.1.2 on 2020-10-28 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20201028_1905'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date', '-time']},
        ),
    ]
