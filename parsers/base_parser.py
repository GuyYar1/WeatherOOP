from abc import ABC, abstractmethod
from utils.event import Event

class BaseParser(ABC):
    """This is the abstract base class for all parsers. """
    def __init__(self):
        self.data_ready_event = Event()
        # breakpoint()

    @abstractmethod
    def fetch_data(self):
        pass