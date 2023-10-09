import json

import requests


def is_valid_json_response(response):
    try:
        response.raise_for_status()
        response.json()
        return True
    except (requests.exceptions.RequestException, json.decoder.JSONDecodeError):
        return False


def is_text_present(response, text):
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
    try:
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException:
        return False
