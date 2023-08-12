from rest_framework import status
from rest_framework.test import APITestCase


class DeliveryTests(APITestCase):
    __url = "/api/rates/"

    def test_correct_data_real_requests(self):
        value = 1
        diff = 17
        float_digits = 4
        correct_data = [
            {"from": "RUB", "to": "EUR", "value": value},
            {"from": "RUB", "to": "EUR", "value": value * diff},
        ]

        result = []

        for test_case in correct_data:
            response = self.client.get(self.__url, data=test_case)

            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK,
                (
                    "Убедитесь, что /api/rates/ работает корректно на "
                    "корректных данных",
                ),
            )
            self.assertIn(
                "result", response.json(), "В ответе нет ключа result"
            )
            result.append(response.json()["result"])

        first_value = result[0]
        second_value = result[1]
        self.assertEqual(
            round(first_value * diff, float_digits),
            round(second_value, float_digits),
        )

    def test_incorrect_data_real_requests(self):
        incorrect_data = [
            {"from": "RU", "to": "EUR", "value": 127},
            {"from": "RUB", "to": "EUR", "value": "aaa"},
            {"from": "RU", "to": "EUR"},
        ]
        for test_case in incorrect_data:
            with self.subTest(test_case=test_case):
                response = self.client.get(self.__url, data=test_case)
                self.assertEqual(
                    response.status_code,
                    status.HTTP_400_BAD_REQUEST,
                    (
                        "Убедитесь, что /api/rates/ работает корректно на "
                        "некорректных данных",
                    ),
                )
