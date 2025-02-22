# Generated by Django 4.0.4 on 2022-05-08 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_providers_ldap", "0001_squashed_0005_ldapprovider_search_mode"),
    ]

    operations = [
        migrations.AddField(
            model_name="ldapprovider",
            name="bind_mode",
            field=models.TextField(
                choices=[("direct", "Direct"), ("cached", "Cached")], default="direct"
            ),
        ),
    ]
