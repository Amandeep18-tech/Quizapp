# Generated by Django 3.1.4 on 2020-12-30 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('results', models.CharField(max_length=100)),
                ('totalquestions', models.CharField(max_length=100)),
            ],
        ),
    ]
