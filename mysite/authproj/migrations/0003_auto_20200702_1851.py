# Generated by Django 3.0.7 on 2020-07-02 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authproj', '0002_goal_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='currentLogin',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='lastLogin',
        ),
    ]