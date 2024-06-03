class WeatherServicePrinter:

    """
     This class is responsible for printing data and uses dependency injection for the weather manager
    """

    def __init__(self, weather_manager):
        self.weather_manager = weather_manager

    def print_data(self):
        # Command the weather manager to fetch and save data
        self.weather_manager.fetch_and_save_data()
        # Print the data (simulation)
        print("Weather data printed on screen.")