# Generated by Django 5.0.7 on 2024-07-27 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("discussions", "0002_alter_discussion_image_alter_discussion_user"),
        ("users", "0002_rename_user_spyneuser"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discussion",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.spyneuser"
            ),
        ),
    ]
