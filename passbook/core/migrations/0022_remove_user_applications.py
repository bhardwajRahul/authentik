# Generated by Django 2.2 on 2019-04-09 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passbook_core', '0021_policy_timeout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='applications',
        ),
    ]
