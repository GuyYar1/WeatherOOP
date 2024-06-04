from parsers.SpecificParser import *
from services.weather_manager import WeatherManager


class WeatherServicePrinter:

    """
     This class is responsible for printing data and uses dependency injection for the weather manager
    """

    def __init__(self):
        self.weather_manager = WeatherManager()
        self.weather_manager.add_parser(SpecificParser())

    async def print_data(self):
        # Command the weather manager to fetch and save data
        await self.weather_manager.fetch_and_save_data()
        # Print the data (simulation)
        print("Weather data printed on screen.")
