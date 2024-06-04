import asyncio
from parsers.base_parser import BaseParser


class SpecificParser(BaseParser):
    """This is a specific implementation of the parser. """
    async def fetch_data(self):
        # Simulate fetching data
        await asyncio.sleep(20)
        data = {"temp": 25, "humidity": 80}
        # Raise an event when data is ready
        self.data_ready_event.trigger(data)
