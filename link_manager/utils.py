import json

import requests


def is_valid_json_response(response):
    """
    Проверяет, является ли HTTP-ответ допустимым JSON-ответом.

    Args:
        response: Объект HTTP-ответа (requests.Response).

    Returns:
        bool: True, если ответ является допустимым JSON-ответом, False в противном случае.
    """
    try:
        response.raise_for_status()
        response.json()
        return True
    except (requests.exceptions.RequestException, json.decoder.JSONDecodeError):
        return False


def is_text_present(response, text):
    """
    Проверяет, содержит ли ответ указанный текст.

    Args:
        response: Объект HTTP-ответа (requests.Response).
        text (str): Текст, который нужно найти в содержимом ответа.

    Returns:
        bool: True, если текст найден в содержимом ответа, False в противном случае.
    """
    try:
        response.raise_for_status()
        response_text = response.content
        if text.encode('utf-8') in response_text:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False


def is_status_ok(response):
    """
    Проверяет, является ли статус HTTP-ответа успешным (200 OK).

    Args:
        response: Объект HTTP-ответа (requests.Response).

    Returns:
        bool: True, если статус успешный, False в противном случае.
    """
    try:
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException:
        return False
