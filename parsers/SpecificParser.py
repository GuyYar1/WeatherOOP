import asyncio
from parsers.base_parser import BaseParser
from models.weather_data import WeatherData as m
from services.api_gateway_manager import ApiGatewayManager


class SpecificParser(BaseParser):
    """This is a specific implementation of the parser. """
    def __init__(self, city_name: str = None, country_code: str = None):
        super().__init__()   # initiate base class BaseParser
        self.city_name = city_name
        self.country_code = country_code
        # option to add state code.

    async def fetch_data(self):
        # Simulate fetching data
        await asyncio.sleep(2)
         #wc = m(25, 80, 10, "Forcast 3Hours 5 days")  # data = {"temp": 25, "humidity": 80}
        wc=m()  # Empty
        self.city_name = "London"
        self.country_code = None

        #model_weather: WeatherData, city_name: str, country_code: str = None
        apicall = ApiGatewayManager(wc, self.city_name, self.country_code )
        # Consider to remove or think why class is needed here and not static methods utils
        apicall.get_weatherbycity(wc, self.city_name, self.country_code )
        # Raise an event when data is ready
        self.data_ready_event.trigger(wc)
