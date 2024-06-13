import numpy as np
import streamlit as st
from pygments.lexers import python
from services.weather_service_printer import WeatherServicePrinter
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
        weather_service_printer = WeatherServicePrinter()
        # Inside "get_all_forcast" it will generate process and save data inside a queue called:
        # asyncio.create_task(self.queue.producer("Data is ready and saved:", data.serializedata()))
        weather_service_printer.get_all_forcast("Springfield", "US", "IL")

        await weather_service_printer.print_data()
        # a separate thread of the Ui will preform dequeue of get_all_forcast type:  asyncio.Queue()
        # Simulate GUI request to bring and save data which will use
        # st.button("Fetch and Save Weather Data", on_click=weather_service_printer.print_data)




if __name__ == "__main__":
    import asyncio
    asyncio.run(main())



