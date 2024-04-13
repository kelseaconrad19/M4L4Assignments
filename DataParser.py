# 2. WeatherDataParser: Class to parse the weather data from the WeatherDataFetcher and generate a readable report
# Attributes: data from WeatherDataFetcher - data will be a dictionary containing weather information for a specific city
# Example: {"temperature": 70, "condition": "Sunny", "humidity": 50}
# Methods: parse_weather_data(data), generate_report()
class DataParser:
    def __init__(self, data, city):
        self.data = data
        self.city = city

    def parse_detailed_data(self):
        if not self.data or self.city not in self.data:
            return "Weather data not available"
        else:
            city_data = self.data[self.city]
            temperature = city_data["temperature"]
            condition = city_data["condition"]
            humidity = city_data["humidity"]
        detailed_report = f"Weather in {self.city}: {temperature} degrees, {condition}, Humidity: {humidity}%"
        return detailed_report

    def parse_basic_data(self):
        if not self.data or self.city not in self.data:
            return "Weather data not available"
        else:
            city_data = self.data[self.city]
            temperature = city_data["temperature"]
            condition = city_data["condition"]
        basic_report = f"Weather in {self.city}: {temperature} degrees, {condition}"
        return basic_report
