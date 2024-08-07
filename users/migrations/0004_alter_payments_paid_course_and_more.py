# Generated by Django 5.0.6 on 2024-05-31 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0001_initial"),
        ("users", "0003_payments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payments",
            name="paid_course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="materials.course",
            ),
        ),
        migrations.AlterField(
            model_name="payments",
            name="paid_lesson",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="materials.lesson",
            ),
        ),
    ]
