from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class ConverterSerializer(serializers.Serializer):
    """Сериализатор конвертера."""

    current_currency = serializers.SerializerMethodField(
        help_text="Укажите исходную валюту",
    )
    target_currency = serializers.SerializerMethodField(
        help_text="Укажите конечную валюту",
    )
    value = serializers.FloatField(
        help_text="Введите количество", required=True
    )

    class Meta:
        fields = (
            "from",
            "to",
            "value",
        )

    def validate(self, attrs):
        for field in self.Meta.fields:
            if field not in self.initial_data:
                raise ValidationError(f"Обязатальное поле {field}")
        return attrs

    def get_current_currency(self, attrs):
        return self.initial_data["from"]

    def get_target_currency(self, attrs):
        return self.initial_data["to"]
