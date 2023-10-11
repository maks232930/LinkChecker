from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
    """Модель для хранения ссылок и их результатов проверки."""
    CONDITION_CHOICES = (
        ('json', 'JSON-валидный'),
        ('text', 'Есть определенный текст'),
        ('status_code', 'Статус 200'),
    )

    name = models.CharField('Название', max_length=255)
    url = models.URLField('Ссылка')
    condition_type = models.CharField('Условие', max_length=20,
                                      choices=CONDITION_CHOICES)
    text = models.TextField('Текст для поиска', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Работает')
    timestamp = models.DateTimeField(blank=True, null=True,
                                     verbose_name='Время проверки')
    is_result = models.BooleanField('Результат', blank=True, null=True)

    def __str__(self):
        return f'{self.name}: {self.condition_type}'

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
