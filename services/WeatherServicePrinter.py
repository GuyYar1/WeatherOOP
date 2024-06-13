from parsers.h3d5_parser import *
from services.weather_manager import WeatherManager
from services.queue_manager import *


class WeatherServicePrinter:

    """
     This class is responsible for printing data and uses dependency injection for the weather manager
    """

    def __init__(self):
        self.queue_m = Queue_manager()
        self.queue = self.queue_m.create_queues()
        self.weather_manager = WeatherManager(self.queue)


        # Initiate the specificParser for specific APi call

    def get_all_forcast(self, city_name, country_name, state_code):
        self.spi_3h_5d_forecast(city_name, country_name, state_code)

    def spi_3h_5d_forecast(self, city_name, country_name, state_code):
        self.weather_manager.add_parser(H3D5_Parser(city_name, country_name, state_code))

    async def print_data(self):
        # Command the weather manager to fetch and save data
        await self.weather_manager.fetch_and_save_data()
        # Print the data (simulation)
        # Now the data of the parsers are inside the queue, call the UI print
        print("Weather data printed on screen.")
