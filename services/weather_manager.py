import tracemalloc
import requests
import asyncio
import datetime
from models.cache import *
from models.weather_data import WeatherData as m
from parsers.base_parser import BaseParser
from utils.event import Event
from services.queue_manager import Queue_manager

# import pdb ## Enable trace while using the run and not the debug mode

class WeatherManager:
    """This class manages the parsers and commands them to fetch data. """
    def __init__(self):
        self.parsers = []  # List to hold different parsers
        self.data_ready_event = Event()
        self.queue_m = Queue_manager()

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
        #breakpoint()
        # tracemalloc.start()
        # snapshot = tracemalloc.take_snapshot()
        # top_stats = snapshot.statistics('lineno')
        # Start the producer and consumer tasks
        # breakpoint()
        # producer_task = await asyncio.create_task(self.queue_m.add_to_queue(
        #                                     "Data is ready and saved:" + str(data.serializedata())
        #                                     ))

        serialized_data = await data.serializedata()

        # Start the producer task
        producer_task = await self.queue_m.add_to_queue(
            "Data is ready and saved: " + str(serialized_data)
        )

        # await asyncio.gather(producer_task) # is there a meaning for only producer_task - check
        print("on_data_ready")
        # for stat in top_stats[:10]:
        #     print(stat)
        # breakpoint()

    async def get_from_queue(self):
        return await self.queue_m.get_next_item()

