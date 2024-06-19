from parsers.h3d5_parser import *
from services.weather_manager import WeatherManager


class WeatherServicePrinter:
    """
     This class is responsible for printing data and uses dependency injection for the weather manager
    """

    def __init__(self):
        self.weather_manager = WeatherManager()
        # Initiate the specificParser for specific APi call

    def get_all_forcast(self, city_name, country_code, state_code):
        self.spi_3h_5d_forecast(city_name, country_code, state_code)

    def spi_3h_5d_forecast(self, city_name, country_code, state_code):
        self.weather_manager.add_parser(H3D5_Parser(city_name, country_code, state_code))

    def print_data(self):
        # Command the weather manager to fetch and save data
        self.weather_manager.fetch_and_save_data()

    def get_from_queue(self):
        #  item = {"aggrtext": "", "dataplot": {}}
        item = self.weather_manager.get_from_queue()
        return item
