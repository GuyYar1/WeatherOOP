class WeatherData:
    """This file contains the data model. """
    def __init__(self, temp, humidity):
        self.temp = temp
        self.humidity = humidity

    def serializedata(self):
        """Serialize the data to a dictionary"""

        return {
            "temperature": self.temp,
            "humidity": self.humidity
        }
