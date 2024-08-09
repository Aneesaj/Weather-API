import requests

api_key = '507fdd3c8d89d294e99d86d0cd7f2616'

city = input('Enter city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    pres = data['main']['pressure']
    humi = data['main']['humidity']
    tempC= temp-273.15
    desc = data['weather'][0]['description']
    
    
    print(f'TEMPERATURE: {tempC} °C')
    print(f'PRESSURE: {pres} atm')
    print(f'HUMIDITY: {humi} %')
    
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')