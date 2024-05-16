import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_seasonal_weather(self):
        response = self.app.get('/seasonalWeather')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('outlook', data)

    def test_get_planting_suggestion(self):
        response = self.app.get('/plantingSuggestion?crop=Fruit')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('suggestion', data)

    def test_report_rainfall(self):
        response = self.app.post('/reportRainfall', data={'rainfall': '10mm'})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', data)

    def test_get_indigenous_knowledge(self):
        response = self.app.get('/indigenousKnowledge?topic=weather prediction')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('info', data)

    def test_get_agricultural_knowledge(self):
        response = self.app.get('/agriculturalKnowledge?category=soil')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('tip', data)

    def test_manage_alert_subscription(self):
        response = self.app.get('/alertSubscribe?type=day')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('status', data)

    def test_leave_message(self):
        response = self.app.post('/message', data={'message': 'Hello, world!'})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', data)

if __name__ == '__main__':
    unittest.main()
