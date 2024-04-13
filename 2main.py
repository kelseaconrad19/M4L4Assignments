from DataFetcher import WeatherDataFetcher
from DataParser import DataParser
from UserInterface import UserInterface

"""A main.py script that demonstrates how the different modules and classes come 
together to form a fully functional weather forecast application. The script should 
exemplify the benefits of using OOP and modular programming in Python.
"""
city = input("What city would you like to get the weather forecast for? ")

weather_fetcher = WeatherDataFetcher("weather_data.txt")
data_parser = DataParser(weather_fetcher.fetch_weather_data(), city)
user_interface = UserInterface(data_parser)

user_interface.display_weather(city)
