# Generated by Django 3.1.2 on 2020-10-28 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201028_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now_add=True, default='2020-01-01'),
            preserve_default=False,
        ),
    ]