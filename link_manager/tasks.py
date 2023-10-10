import requests
from celery import shared_task
from django.utils import timezone

from .models import Link
from .utils import is_valid_json_response, is_text_present, is_status_ok


@shared_task
def main_task():
    """
    Основная задача для проверки всех активных ссылок.

    Эта задача вызывает `web_data_fetcher` для каждой активной ссылки в базе данных.
    """
    links = Link.objects.filter(is_active=True)

    for link in links:
        web_data_fetcher.delay(link.pk)


@shared_task
def web_data_fetcher(link_id):
    """
    Задача для проверки конкретной ссылки.

    Параметры:
    link_id (int): Идентификатор ссылки, которую нужно проверить.

    Если ссылка существует и активна, эта задача отправляет HTTP-запрос по URL ссылки.
    В зависимости от типа условия (json, text или status_code), проверяется ответ на соответствие
    критериям. Результат проверки сохраняется в объекте Link в полях `timestamp` и `is_result`.
    """
    try:
        link = Link.objects.get(pk=link_id)
        response = requests.get(link.url)
        is_valid = False

        if link.condition_type == 'json':
            is_valid = is_valid_json_response(response)
        elif link.condition_type == 'text':
            is_valid = is_text_present(response, link.text)
        elif link.condition_type == 'status_code':
            is_valid = is_status_ok(response)

        link.timestamp = timezone.now()
        link.is_result = is_valid
        link.save()
    except Link.DoesNotExist:
        pass
