from django.conf import settings

from .services import _send_request
from .validators import _validate_currencies, _validate_keys


def _get_body(data):
    """Формирование тела запроса."""
    return {
        "from": data["current_currency"],
        "to": data["target_currency"],
        "amount": data["value"],
    }


def _get_params():
    """Формирование хедеров."""
    return {
        "access_key": settings.API_KEY,
    }


def _calculate_value(latest_data, current_data):
    """Расчет окончательного значения."""
    value = current_data["value"]
    current_currency = current_data["current_currency"]
    target_currency = current_data["target_currency"]
    euro_to_current_currency = latest_data.get(current_currency)
    euro_to_target_currency = latest_data.get(target_currency)
    _validate_currencies(
        (target_currency, euro_to_target_currency),
        (current_currency, euro_to_current_currency),
    )
    return euro_to_target_currency * value / euro_to_current_currency


def get_converted_value(data):
    """Основаная логика получения ответа."""
    body = _get_body(data)
    params = _get_params()
    exchange_rates = _send_request(
        url=settings.EXCHANGE_ENDPOINT,
        method="POST",
        body=body,
        params=params,
    )
    _validate_keys(exchange_rates, "rates")
    return _calculate_value(exchange_rates["rates"], data)
