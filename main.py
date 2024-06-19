import os
import time

import services.plot_data
from services.WeatherServicePrinter import *
from services.weather_manager import *
from parsers.h3d5_parser import *
from UI.tcl_ui_app import *
from utils.debug_print import debug_print
import pdb

# Set this environment variable in your development environment
# For example, in Unix-based systems: export DEBUG_MODE='true'

DEBUG_MODE = True


def main():

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
        os.system('cls')

        print("Wellcome... select please: ")
        # Inject the weather manager into the printer
        city_name = input("Please Type city_name: (e.g:Springfield) -->")
        state_code = input("Please Type state_code: (e.g:IL) -->")

        country_code = input("Please Type country_code: (e.g:US) -->")

        weather_srv_obj = WeatherServicePrinter()

        # # Inside "get_all_forcast" it will generate process and save data inside a queue called:
        weather_srv_obj.get_all_forcast(city_name, country_code, state_code)  # #("Springfield", "US", "IL")
        weather_srv_obj.print_data()
        # a separate thread of the Ui will preform dequeue of get_all_forcast type:  asyncio.Queue()
        # Simulate GUI request to bring and save data which will use
        # while True:
        # await asyncio.sleep(10)  # Delay for 2 seconds
        print("get_from_queue")
        next_item = weather_srv_obj.get_from_queue()
        if next_item["aggrtext"] == "No other Item, all is dequeued":
            print(next_item["aggrtext"])
            print("No other Item @@")
            #break

        elif "The current time is" in next_item["aggrtext"]:
            # There is data
            print(next_item["aggrtext"])
            debug_print("-" * 20)
        else:
            debug_print('Failed to retrieve weather data.')
            # async for strprint in queue_manager.consumer(): Yield not return
            # print("-" * 20)


if __name__ == "__main__":
    import asyncio
    main()



