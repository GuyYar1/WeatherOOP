from parsers.base_parser import *
from services.queue_manager import *
from utils.event import *


class WeatherManager:
    """This class manages the parsers and commands them to fetch data. """
    def __init__(self):
        self.parsers = []  # List to hold different parsers
        self.data_ready_event = Event()
        self.queue_m = Queue_manager()

    def add_parser(self, parser: BaseParser):
        self.parsers.append(parser)
        self.parsers[-1].data_ready_event += self.on_data_ready
        # when data_ready_event of the parser itself which came from the BaseParser is triggered (wc)
        # the handler will be set to the WeatherManager function: on_data_ready
        # so when the parser event triggered the WeatherManager on_data_ready is called and executed.


    def fetch_and_save_data(self):
        for parser in self.parsers:
            parser.fetch_data()

    def on_data_ready(self, data):
        """This will append self.on_data_ready to the list of handlers for the last parser’s data_ready_event.
         When trigger is called on that event, it will execute all handlers in the list.
          If self.on_data_ready is an asynchronous function,
         it will be scheduled as a task in the event loop; otherwise, it will be called directly."""
        # Handle the event when data is ready, so first do fetch
        serialized_data = data.serializedata()
        # Start the producer task
        print("add_to_queue")
        self.queue_m.add_to_queue(
            "Data is ready and saved: " + serialized_data
        )


    def get_from_queue(self):
        return self.queue_m.get_next_item()

