# Generated by Django 4.2.2 on 2023-06-21 11:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0006_rename_master_organization"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Organization",
            new_name="Master",
        ),
    ]