from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
    CONDITION_CHOICES = (
        ('json', 'JSON-валидный'),
        ('text', 'Есть определенный текст'),
        ('status_code', 'Статус 200'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=255)
    url = models.URLField('Ссылка')
    condition_type = models.CharField('Условие', max_length=20, choices=CONDITION_CHOICES)
    text = models.TextField('Текст для поиска', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Работает')

    def __str__(self):
        return f'{self.name}: {self.condition_type}'

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'


class Result(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_result = models.BooleanField('Результат')

    def __str__(self):
        return self.link.link

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
