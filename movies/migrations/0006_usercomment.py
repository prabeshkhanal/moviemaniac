# Generated by Django 2.2.5 on 2020-02-15 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_remove_movie_movieid'),
    ]

    operations = [
        migrations.CreateModel(
            name='usercomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('rating', models.IntegerField(max_length=100)),
                ('comment', models.CharField(max_length=100)),
            ],
        ),
    ]