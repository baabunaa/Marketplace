# Generated by Django 3.1.2 on 2020-10-28 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_post_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['date']},
        ),
    ]