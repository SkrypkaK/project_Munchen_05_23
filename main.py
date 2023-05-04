import requests
# импорт модуля для работы и запросов с HTTP
API_KEY = '2c03e5bdaf9be012266b4038a54600ec'  # указываю  свой ключ API OpenWeatherMap.
API_URL = 'https://api.openweathermap.org/data/2.5'   # адрес API с которого берем данные погоды
UNIT = 'metric'  # изменить на цельсий для данных по Фарингейту

# Ввод наименования города
city_name = input('Enter city name: ')

# Сделать запрос API для получения текущих данных о погоде.  f - обьявление формата строки позволяющее
# вставлять значение переменных. ?q - параметр запроса который содержит название города,
# {} - операторы строки которые позволяют вставлять значение переменных внутрь строки
# response = requests.get....ответ равняется запросу к библиотеке requests. и get получить данные из нашего url
current_weather_url = f'{API_URL}/weather?q={city_name}&units={UNIT}&appid={API_KEY}'
current_weather_response = requests.get(current_weather_url)

# запрос  API данных о погоде - прогноз
forecast_url = f'{API_URL}/forecast?q={city_name}&units={UNIT}&appid={API_KEY}'
forecast_response = requests.get(forecast_url)
# если статус кода будет равняться 200 то...
if current_weather_response.status_code == 200 and forecast_response.status_code == 200:
 # положительные запросы  API
 # json - это метод response который позволяет   работать с данными в формате JSON в Python
 # и взаимодействовать с внешними сервисами и API, которые используют JSON для передачи данных.
 #  в данном случае мы получая данные от внешнего АРІ в формате  декодируем их в обьект Python для дальнейшего использования

    current_weather_data = current_weather_response.json()
    forecast_data = forecast_response.json()

 # вывод на косоль данных
    print('Current Weather Information for', city_name)
    print('Temperature:', current_weather_data['main']['temp'], '°C')
    print('Weather Description:', current_weather_data['weather'][0]['description'])
    print('Humidity:', current_weather_data['main']['humidity'], '%')
    print('Wind Speed:', current_weather_data['wind']['speed'], 'm/s')

 # вывод на консоль данных на 5 дней
    print('5-day Forecast for', city_name)
    for forecast in forecast_data['list']:
        print('Date:', forecast['dt_txt'])
        print('Temperature:', forecast['main']['temp'], '°C')
        print('Weather Description:', forecast['weather'][0]['description'])
        print('Humidity:', forecast['main']['humidity'], '%')
        print('Wind Speed:', forecast['wind']['speed'], 'm/s')
        print('---')
else:
    # негативный ответ API
    print('Failed to retrieve weather information. Error:', current_weather_response.status_code,
          forecast_response.status_code)


