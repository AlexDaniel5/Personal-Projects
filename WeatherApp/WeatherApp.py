import requests

apiKey = 'd3c9e0419c37be8e02d1a4ed7bc49035'
city = input("Enter a city: ")
#Uses the request library to go and fetch the url which provides an extensive list of the forecast in a city
weatherData = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={apiKey}")
#print(weatherData.json()) #Here for debugging purposes
#If the status code of the api which it returns is equal to 404, it means the city doesn't exist on the webpage
if weatherData.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weatherData.json()['weather'][0]['description']
    temp = weatherData.json()['main']['temp']
    feelsLike = weatherData.json()['main']['feels_like']
    humidity = weatherData.json()['main']['humidity']
    print(f"The Forecast of {city}")
    print(f"Weather: {weather}")
    print(f"Temperature: {temp}°C")
    print(f"Feels like: {feelsLike}°C")
    print(f"Humidity: {humidity}%")
