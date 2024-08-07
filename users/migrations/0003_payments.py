# Generated by Django 5.0.6 on 2024-05-31 19:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0001_initial"),
        ("users", "0002_remove_user_username_user_avatar_user_city_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "payment_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата платежа"
                    ),
                ),
                ("total", models.FloatField(verbose_name="Сумма платежа")),
                (
                    "payment_method",
                    models.CharField(
                        choices=[("cash", "Наличные"), ("bank", "Банковская карта")],
                        default="bank",
                        max_length=10,
                        verbose_name="Способ оплаты",
                    ),
                ),
                (
                    "paid_course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.course",
                    ),
                ),
                (
                    "paid_lesson",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.lesson",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Платеж",
                "verbose_name_plural": "Платежи",
                "ordering": ("-payment_date",),
            },
        ),
    ]
