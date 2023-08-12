import requests
from django.conf import settings
from rest_framework.exceptions import ParseError, ValidationError


def _send_request(url, method, body=None, params=None, headers=None):
    """Отправка запроса."""
    mapper = {
        "GET": requests.get,
        "POST": requests.post,
    }
    try:
        return mapper[method](
            url=url,
            params=params,
            timeout=settings.REQUEST_TIMEOUT,
        ).json()
    except requests.exceptions.ConnectionError:
        raise ParseError(f"Ошибка соединения с API {url}")
    except requests.exceptions.JSONDecodeError:
        raise ValidationError("API вернул не сериализуемый формат")
    except Exception as error:
        raise ParseError(f"Непредвиденная ошибка {type(error)} {error}")
