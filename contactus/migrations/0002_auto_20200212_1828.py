# Generated by Django 2.2.5 on 2020-02-12 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='user_full_name',
            new_name='user_fullname',
        ),
    ]
