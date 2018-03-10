import requests

r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Baulne,fr&appid=aecef374984aecf5c205fb2d974115ac")
temp = float(r.json()['main']['temp'])
temp -= 273.15
temp = round(temp, 1)
print(r.json())
print(r.json()['weather'][0]['main'])
