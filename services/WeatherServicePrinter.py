from parsers.h3d5_parser import *
from services.weather_manager import WeatherManager


class WeatherServicePrinter:
    """
     This class is responsible for printing data and uses dependency injection for the weather manager
    """

    def __init__(self):
        self.weather_manager = WeatherManager()
        # Initiate the specificParser for specific APi call

    async def get_all_forcast(self, city_name, country_code, state_code):
        await self.spi_3h_5d_forecast(city_name, country_code, state_code)

    async def spi_3h_5d_forecast(self, city_name, country_code, state_code):
        await self.weather_manager.add_parser(H3D5_Parser(city_name, country_code, state_code))

    async def print_data(self):
        # Command the weather manager to fetch and save data
        await self.weather_manager.fetch_and_save_data()
        # Print the data (simulation)
        # Now the data of the parsers are inside the queue, call the UI print
        # print("Weather data printed on screen.")

    async def get_from_queue(self):
        item = await self.weather_manager.get_from_queue()
        return item
