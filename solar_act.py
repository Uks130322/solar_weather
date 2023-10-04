"""Coronal Mass Ejection (CME)
startDate: default to 30 days prior to current UTC date
endDate: default to current UTC date

Example:
https://api.nasa.gov/DONKI/CME?startDate=yyyy-MM-dd&endDate=yyyy-MM-dd&api_key=DEMO_KEY"""

import requests
import json
import csv
from openpyxl import Workbook
from pprint import pprint as pp

response = requests.get("https://api.nasa.gov/DONKI/CME?"
                         "startDate=2023-07-20&endDate=2023-07-25"
                         "&api_key=DEMO_KEY")

weather = response.json()

outfile = open("solar_data_01.json", "w")
json.dump(weather, outfile)
outfile.close()
json.dumps(weather)
print(json.dumps(weather, indent=2))

wb = Workbook()
ws = wb.active
ws.title = "Weather data"

result = json.loads(response.text)
weather_keys = list(result[0].keys())
print(weather_keys)
for data in weather:
    csv.DictWriter(open("sun_weather.csv", "a"), weather_keys).writerow(data)
for row in csv.reader(open("sun_weather.csv")):
    ws.append(row)

wb.save("solar_weather.xlsx")
