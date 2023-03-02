def forecast(*args):
    weather_dict = {
        "Sunny": [],
        "Cloudy": [],
        "Rainy": [],
    }

    result = ""
    for location, weather in args:
        weather_dict[weather].append(location)

    for weather, locations in weather_dict.items():
        locations = sorted(locations, key=lambda x: x)
        if locations:
            for location in locations:
                result += f'{location} - {weather}\n'
    return result




print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
