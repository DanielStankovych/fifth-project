# Generated by Django 2.2.4 on 2019-10-24 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forumapp', '0005_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='slug',
            new_name='post_slug',
        ),
    ]
