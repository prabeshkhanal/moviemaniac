# Generated by Django 2.2.5 on 2020-02-10 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_photo', models.CharField(max_length=100)),
                ('movie_name', models.CharField(max_length=100)),
                ('movie_date', models.CharField(max_length=100)),
            ],
        ),
    ]
