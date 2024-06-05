import asyncio
from parsers.base_parser import BaseParser
from models.weather_data import WeatherData as m

class SpecificParser(BaseParser):
    """This is a specific implementation of the parser. """
    async def fetch_data(self):
        # Simulate fetching data
        await asyncio.sleep(10)
        wc = m(25, 80)  # data = {"temp": 25, "humidity": 80}

        # Raise an event when data is ready
        self.data_ready_event.trigger(wc)
