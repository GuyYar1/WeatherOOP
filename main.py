from services.WeatherServicePrinter import WeatherServicePrinter
from services.weather_manager import WeatherManager
from parsers.h3d5_parser import H3D5_Parser
from UI.tcl_ui_app import *

async def main():
    """Explanation
Main File: main.py initializes the necessary components and handles the GUI interaction using Streamlit.
Weather Service Printer: Responsible for printing data and uses dependency injection for the WeatherManager.
Weather Manager: Manages different parsers, commands them to fetch data, and handles data ready events.
Parsers: Abstract base parser and specific implementations for different APIs.
Models: Defines the data model structure.
Utils: Contains utility functions and classes, such as the event handling mechanism.
This structure ensures clear separation of concerns, making the codebase modular and easy to extend. Each component has a well-defined responsibility, and the use of abstract base classes and event handling allows for flexible and asynchronous operations.
"""
    while True:
        # Inject the weather manager into the printer
        weather_srv_obj = WeatherServicePrinter()# Inside "get_all_forcast" it will generate process and save data inside a queue called:
        weather_srv_obj.get_all_forcast("Springfield", "US", "IL")
        await weather_srv_obj.print_data()
        # a separate thread of the Ui will preform dequeue of get_all_forcast type:  asyncio.Queue()
        # Simulate GUI request to bring and save data which will use
        while True:
            next_item = await weather_srv_obj.get_from_queue()
            print(next_item)
            print("-" * 20)
        else:
            print('Failed to retrieve weather data.')
            # async for strprint in queue_manager.consumer(): Yield not return
            print("-" * 20)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())



