'''import requests'''

def get_weather_desc_and_temp():
    api_key = "123456789abcdefg"
    from aiohttp import request
    city = "Orlando"
    url = "enterurlhere"

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'description': description,
            'temp_min': temp_min,
            'temp_max': temp_max}

def main():
    weather_dict = get_weather_desc_and_temp()

    print(f"Today's forecast is {weather_dict.get('description')}")
    print(f"The minimum temperature is {weather_dict.get('temp_min')}")
    print(f"The maximum temperature is {weather_dict.get('temp_max')}")

main()