# Generated by Django 2.2.5 on 2020-02-15 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_photo', models.ImageField(upload_to='')),
                ('movie_name', models.CharField(max_length=100)),
                ('movie_date', models.CharField(max_length=100)),
                ('movie_description', models.CharField(default='', max_length=1000)),
                ('movie_genre', models.CharField(default='', max_length=250)),
            ],
        ),
    ]