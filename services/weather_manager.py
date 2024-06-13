import requests
import asyncio
import datetime
from models.cache import *
from models.weather_data import WeatherData as m
from parsers.base_parser import BaseParser
from utils.event import Event
# import pdb ## Enable trace while using the run and not the debug mode

class WeatherManager():
    """This class manages the parsers and commands them to fetch data. """
    def __init__(self, queue):
        self.parsers = []  # List to hold different parsers
        self.data_ready_event = Event()
        self.queue = queue



    def add_parser(self, parser: BaseParser):
        self.parsers.append(parser)
        # when data_ready_event of the parser itself which came from the BaseParser is triggered (wc)
        # the handler will be set to the WeatherManager function: on_data_ready
        # so when the parser event triggered the WeatherManager on_data_ready is called and executed.
        self.parsers[-1].data_ready_event += self.on_data_ready
        # breakpoint()

    async def fetch_and_save_data(self):
        for parser in self.parsers:
            await parser.fetch_data()

    async def on_data_ready(self, data):
        # Handle the event when data is ready, so first do fetch

        # Start the producer and consumer tasks
        producer_task = asyncio.create_task(self.queue.producer(
                                            self.queue, "Data is ready and saved:" + data.serializedata())
                                                                )
        # await asyncio.gather(producer_task) # is there a meaning for only producer_task - check
        print ("on_data_ready")
        
