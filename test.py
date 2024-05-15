import unittest
from app import app, db, Weather, PlantingSuggestion, IndigenousKnowledge, AgriculturalKnowledge, RainfallReport, Message

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        # 清空测试数据库
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_weather(self):
        response = self.app.get('/weather?date=Today')
        data = response.json
        self.assertEqual(response.status_code, 200)
        self.assertIn('forecast', data)

    def test_get_planting_suggestions(self):
        response = self.app.get('/planting?crop=Fruit')
        data = response.json
        self.assertEqual(response.status_code, 200)
        self.assertIn('suggestion', data)

    # 添加更多测试用例...

if __name__ == '__main__':
    unittest.main()
