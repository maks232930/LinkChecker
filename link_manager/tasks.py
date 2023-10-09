import requests
from celery import shared_task

from .models import Link, Result
from .utils import is_valid_json_response, is_text_present, is_status_ok


@shared_task
def main_task():
    links = Link.objects.filter(is_active=True)

    for link in links:
        web_data_fetcher.delay(link.pk)


@shared_task
def web_data_fetcher(link_id):
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

        Result.objects.create(link=link, is_result=is_valid)
    except Link.DoesNotExist:
        pass
