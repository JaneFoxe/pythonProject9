from django.contrib.auth.models import AbstractUser
from django.db import models

NULL_PARAM = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')

    phone = models.CharField(max_length=30, unique=True, verbose_name='Номер телефона', **NULL_PARAM)
    city = models.CharField(max_length=100, verbose_name="Город", null=True)
    avatar = models.ImageField(upload_to="user/", verbose_name="Аватар", **NULL_PARAM)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
