# Generated by Django 3.2.4 on 2021-06-14 15:32

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_stages_identification", "0010_identificationstage_password_stage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="identificationstage",
            name="user_fields",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("email", "E Mail"),
                        ("username", "Username"),
                        ("upn", "Upn"),
                    ],
                    max_length=100,
                ),
                blank=True,
                help_text="Fields of the user object to match against. (Hold shift to select multiple options)",
                size=None,
            ),
        ),
    ]
