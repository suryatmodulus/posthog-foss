# Generated by Django 4.2.11 on 2024-05-28 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0419_remove_organization_available_features"),
    ]

    operations = [
        migrations.CreateModel(
            name="Alert",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("target_value", models.TextField()),
                ("anomaly_condition", models.JSONField(default=dict)),
                ("insight", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="posthog.insight")),
                ("team", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="posthog.team")),
            ],
        ),
    ]
