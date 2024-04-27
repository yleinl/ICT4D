# tests.py

from django.test import TestCase
from django.urls import reverse
from .views import get_weather

class WeatherViewTestCase(TestCase):
    def test_get_weather(self):
        test_cases = [
            ("Today", "Sunny, 24°C"),
            ("One", "Partly cloudy, 22°C"),
            ("Two", "Rainy, 18°C"),
        ]

        for date, expected_forecast in test_cases:
            response = self.client.get(reverse('get_weather'), {'date': date})
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertEqual(data['date'], date)
            self.assertEqual(data['forecast'], expected_forecast)
