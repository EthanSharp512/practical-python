'''import requests'''

'''api_key'''
from aiohttp import request


city = "Orlando"
'''url'''

'''request = requests.get(url'''
json = request.json()

description = json.get("weather")[0].get("description")
print(f"Today's forecast is {description}")
temp_min = json.get("main").get("temp_min")
print(f"The minimum temperature is {temp_min}")
temp_max = json.get("main").get("temp_max")
print(f"The maximum temperature is {temp_max}")