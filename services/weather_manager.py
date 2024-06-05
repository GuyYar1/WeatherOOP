import requests
import asyncio
# import pdb ## Enable trace while using the run and not the debug mode


from models.weather_data import WeatherData as m
from parsers.base_parser import BaseParser
from utils.event import Event

class WeatherManager:
    """This class manages the parsers and commands them to fetch data. """
    def __init__(self):
        self.parsers = []  # List to hold different parsers
        self.data_ready_event = Event()

    def add_parser(self, parser: BaseParser):
        self.parsers.append(parser)
        self.parsers[-1].data_ready_event += self.on_data_ready
        # breakpoint()

    async def fetch_and_save_data(self):
        for parser in self.parsers:
            await parser.fetch_data()

    def on_data_ready(self, data):
        # Handle the event when data is ready
        print("Data is ready and saved:", data.serializedata())
