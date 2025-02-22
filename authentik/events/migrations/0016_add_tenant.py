# Generated by Django 3.2.4 on 2021-06-14 15:33

from django.db import migrations, models

import authentik.events.models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_events", "0015_alter_event_action"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="tenant",
            field=models.JSONField(blank=True, default=authentik.events.models.default_tenant),
        ),
        migrations.AlterField(
            model_name="event",
            name="action",
            field=models.TextField(
                choices=[
                    ("login", "Login"),
                    ("login_failed", "Login Failed"),
                    ("logout", "Logout"),
                    ("user_write", "User Write"),
                    ("suspicious_request", "Suspicious Request"),
                    ("password_set", "Password Set"),
                    ("secret_view", "Secret View"),
                    ("invitation_used", "Invite Used"),
                    ("authorize_application", "Authorize Application"),
                    ("source_linked", "Source Linked"),
                    ("impersonation_started", "Impersonation Started"),
                    ("impersonation_ended", "Impersonation Ended"),
                    ("policy_execution", "Policy Execution"),
                    ("policy_exception", "Policy Exception"),
                    ("property_mapping_exception", "Property Mapping Exception"),
                    ("system_task_execution", "System Task Execution"),
                    ("system_task_exception", "System Task Exception"),
                    ("system_exception", "System Exception"),
                    ("configuration_error", "Configuration Error"),
                    ("model_created", "Model Created"),
                    ("model_updated", "Model Updated"),
                    ("model_deleted", "Model Deleted"),
                    ("email_sent", "Email Sent"),
                    ("update_available", "Update Available"),
                    ("custom_", "Custom Prefix"),
                ]
            ),
        ),
    ]
