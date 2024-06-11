import requests

def get_weather(city):
    api_key = "304f4f579a895a521d335fb3c99ac2b9"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        temperature = main["temp"]
        weather_description = data["weather"][0]["description"]
        return f"Temperature: {temperature - 273.15:.2f}°C\nDescription: {weather_description}"
    else:
        return "City not found."

