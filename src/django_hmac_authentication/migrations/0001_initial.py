# Generated by Django 4.1.7 on 2023-05-08 01:15

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ApiHMACKey",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified_on", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "secret",
                    models.CharField(
                        editable=False, max_length=512, verbose_name="Secret"
                    ),
                ),
                (
                    "salt",
                    models.CharField(
                        editable=False, max_length=80, verbose_name="Salt"
                    ),
                ),
                ("revoked", models.BooleanField(default=False, verbose_name="Revoked")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="api_secrets",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "API Secret",
                "verbose_name_plural": "API Secrets",
            },
        ),
    ]
