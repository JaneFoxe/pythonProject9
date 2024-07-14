from django.contrib.auth.models import AbstractUser
from django.db import models

NULL_PARAM = {"null": True, "blank": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Почта")

    phone = models.CharField(
        max_length=30, unique=True, verbose_name="Номер телефона", **NULL_PARAM
    )
    city = models.CharField(max_length=100, verbose_name="Город", null=True)
    avatar = models.ImageField(upload_to="user/", verbose_name="Аватар", **NULL_PARAM)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payments(models.Model):
    PAYMENT_METHODS = (
        ("cash", "Наличные"),
        ("bank", "Банковская карта"),
    )

    user = models.ForeignKey("users.User", on_delete=models.SET_NULL,
                             **NULL_PARAM,
                             verbose_name="Пользователь", )
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата платежа")
    paid_course = models.ForeignKey(
        "materials.Course", on_delete=models.CASCADE, **NULL_PARAM
    )
    paid_lesson = models.ForeignKey(
        "materials.Lesson", on_delete=models.CASCADE, **NULL_PARAM
    )
    total = models.PositiveIntegerField(verbose_name="Сумма платежа")
    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHODS,
        default="bank",
        verbose_name="Способ оплаты",
    )
    link = models.URLField(
        max_length=400,
        **NULL_PARAM,
        verbose_name="Ссылка на оплату"
    )
    session_id = models.CharField(
        max_length=255,
        **NULL_PARAM,
        verbose_name="id сессии"
    )
    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ("-payment_date",)

    def __str__(self):
        return self.total
