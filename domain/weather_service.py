from infra.weather_provider import get_weather




def get_weather_string(city):
    info=get_weather(city)


    return f"Weather in {info['city']} is {info['temperature']}°C and {info['condition']}. Have a great day"

