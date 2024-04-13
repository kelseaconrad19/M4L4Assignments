import json
# 1. WeatherDataFetcher: Class to fetch weather data for a given city from the original data source
# Attributes: city, original data source
# The original data source will be a local text file that contains weather data for different cities in the form of a dictionary (e.g., {"New York": {"temperature": 70, "condition": "Sunny", "humidity": 50}})
# Methods: fetch_weather_data(city)


class WeatherDataFetcher:
    def __init__(self, data_source):
        self.data_source = data_source

    def fetch_weather_data(self):
        with open(self.data_source, 'r') as file:
            weather_data = json.load(file)
        return weather_data
