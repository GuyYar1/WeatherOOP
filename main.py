import streamlit as st
from services.weather_service_printer import WeatherServicePrinter
from services.weather_manager import WeatherManager
from parsers.specific_parser import SpecificParser

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

    # Initialize the weather manager and parser
    weather_manager = WeatherManager()
    specific_parser = SpecificParser()

    # Inject the weather manager into the printer
    weather_service_printer = WeatherServicePrinter(weather_manager)

    # Simulate GUI request to bring and save data
    st.button("Fetch and Save Weather Data", on_click=weather_service_printer.print_data)


if __name__ == "__main__":
    main()