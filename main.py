from services.WeatherServicePrinter import *
from services.weather_manager import *
from parsers.h3d5_parser import *
from UI.tcl_ui_app import *
import os

# Set this environment variable in your development environment
# For example, in Unix-based systems: export DEBUG_MODE='true'
debug_mode = os.getenv('DEBUG_MODE') == 'true'

def debug_print(*args):
    """print can block the async function flow so print only if you are in debug mode"""
    if debug_mode:
        print(*args)

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
    # while True:
        ## print("Wellcome... select please: ")
        # Inject the weather manager into the printer
        # city_name = input("Please Type city_name: (e.g:Springfield) -->")
        # country_code = input("Please Type country_code: (e.g:US) -->")
        # state_code = input("Please Type state_code: (e.g:IL) -->")

    weather_srv_obj = WeatherServicePrinter()

    # # Inside "get_all_forcast" it will generate process and save data inside a queue called:
    await weather_srv_obj.get_all_forcast("Springfield", "US", "IL")   # (city_name, country_code, state_code)
    await weather_srv_obj.print_data()
    # a separate thread of the Ui will preform dequeue of get_all_forcast type:  asyncio.Queue()
    # Simulate GUI request to bring and save data which will use
    while True:
        await asyncio.sleep(5)  # Delay for 5 seconds
        next_item = await weather_srv_obj.get_from_queue()
        if next_item == "No other Item, all is dequeued":
            print(next_item)
            break
        elif "The current time is" in next_item:
            # There is data
            print(next_item)
            print("-" * 20)
        else:
            print('Failed to retrieve weather data.')
            # async for strprint in queue_manager.consumer(): Yield not return
            # print("-" * 20)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())



