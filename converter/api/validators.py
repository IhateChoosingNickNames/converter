from rest_framework.exceptions import ValidationError


def _validate_currencies(*currencies):
    """Валидатор валют."""
    for currency, value in currencies:
        if value is None:
            raise ValidationError(f"Некорректное название валюты {currency}")


def _validate_keys(reponse, *keys):
    """Валидатор ключей."""
    for key in keys:
        if key not in reponse:
            raise ValidationError(f"В ответе нет ключа {key}")
