# Generated by Django 3.1.4 on 2021-01-04 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='results',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
