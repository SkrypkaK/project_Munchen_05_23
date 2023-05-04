import unittest
import requests
# Тест определяет два метода, которые проверяют текущую погоду и прогноз соответственно.
# Каждый тест отправляет запрос в API, утверждает, что код состояния ответа равен 200 (т. е. OK),
# а затем проверяет данные ответа на наличие ожидаемой структуры и значений.

class TestWeatherAPI(unittest.TestCase):
    def setUp(self):
        self.API_KEY = '2c03e5bdaf9be012266b4038a54600ec'
        self.API_URL = 'https://api.openweathermap.org/data/2.5'
        self.UNIT = 'metric'
        self.city_name = 'New York'

    def test_current_weather(self):
        current_weather_url = f'{self.API_URL}/weather?q={self.city_name}&units={self.UNIT}&appid={self.API_KEY}'
        current_weather_response = requests.get(current_weather_url)
        self.assertEqual(current_weather_response.status_code, 200)
        # assertEqual метод из unittest модуля,
        # чтобы проверить, равен ли код состояния HTTP объекта ответа 200, что указывает на успешный ответ.

        current_weather_data = current_weather_response.json()
        self.assertIn('main', current_weather_data)
        self.assertIn('temp', current_weather_data['main'])
        self.assertIn('weather', current_weather_data)
        self.assertTrue(isinstance(current_weather_data['weather'], list))
        self.assertGreater(len(current_weather_data['weather']), 0)
        # метод, чтобы проверить, weather является ли ключ списком, и метод,
        # чтобы проверить, больше assertGreater()ли длина списка нуля.weather
        self.assertIn('description', current_weather_data['weather'][0])
        self.assertIn('humidity', current_weather_data['main'])
        self.assertIn('wind', current_weather_data)
        self.assertIn('speed', current_weather_data['wind'])

    def test_forecast(self):
        forecast_url = f'{self.API_URL}/forecast?q={self.city_name}&units={self.UNIT}&appid={self.API_KEY}'
        forecast_response = requests.get(forecast_url)
        self.assertEqual(forecast_response.status_code, 200)

        forecast_data = forecast_response.json()
        self.assertIn('list', forecast_data)
        self.assertTrue(isinstance(forecast_data['list'], list))
        self.assertGreater(len(forecast_data['list']), 0)

        for forecast in forecast_data['list']:
            self.assertIn('dt_txt', forecast)
            self.assertIn('main', forecast)
            self.assertIn('temp', forecast['main'])
            self.assertIn('weather', forecast)
            self.assertTrue(isinstance(forecast['weather'], list))
            self.assertGreater(len(forecast['weather']), 0)
            self.assertIn('description', forecast['weather'][0])
            self.assertIn('humidity', forecast['main'])
            self.assertIn('wind', forecast)
            self.assertIn('speed', forecast['wind'])
# Для каждого прогноза функция проверяет наличие ключей 'dt_txt', 'main',  и т.д. а так же в объекте прогноза

if __name__ == '__main__':
    unittest.main()
