from django.db import models

from users.models import NULL_PARAM


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    preview = models.ImageField(upload_to='materials/', verbose_name='Изображение', **NULL_PARAM)
    description = models.TextField(verbose_name="Описание", blank=True)

    def __str__(self):
        # Строковое отображение объекта
        return f"{self.name} | {self.description}"

    class Meta:
        verbose_name = "Курс"  # Настройка для наименования одного объекта
        verbose_name_plural = "Курсы"  # Настройка для наименования набора объектов


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True)
    preview = models.ImageField(upload_to='materials/', verbose_name='Изображение', **NULL_PARAM)
    slug = models.URLField(verbose_name='Ссылка', **NULL_PARAM)
    course = models.ForeignKey(
        "materials.Course",
        on_delete=models.CASCADE,
        verbose_name="Курс",
        related_name="lessons",
        **NULL_PARAM,
    )

    def __str__(self):
        # Строковое отображение объекта
        return f"{self.name} | {self.description}"

    class Meta:
        verbose_name = "Урок"  # Настройка для наименования одного объекта
        verbose_name_plural = "Уроки"  # Настройка для наименования набора объектов
