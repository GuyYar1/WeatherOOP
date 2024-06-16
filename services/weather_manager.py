from parsers.base_parser import *
from services.queue_manager import *
from utils.event import *

from

class WeatherManager:
    """This class manages the parsers and commands them to fetch data. """
    def __init__(self):
        self.parsers = []  # List to hold different parsers
        self.data_ready_event = Event()
        self.queue_m = Queue_manager()

    async def add_parser(self, parser: BaseParser):
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
        """This will append self.on_data_ready to the list of handlers for the last parser’s data_ready_event.
         When trigger is called on that event, it will execute all handlers in the list.
          If self.on_data_ready is an asynchronous function,
         it will be scheduled as a task in the event loop; otherwise, it will be called directly."""
        # Handle the event when data is ready, so first do fetch
        serialized_data = await data.serializedata()
        ## print("serialized_data" + serialized_data)
        # Start the producer task
        await self.queue_m.add_to_queue(
            "Data is ready and saved: " + str(serialized_data)
        )

    async def get_from_queue(self):
        return await self.queue_m.get_next_item()

