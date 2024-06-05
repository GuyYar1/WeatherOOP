from models.cache import Cachebase


class WeatherData(Cachebase):
    """This file contains the data model. """
    def __init__(self, date_time=None, temperature=None, humidity=None, weather_description=None):
        super().__init__() # initiate base class cache
        # instance attributes
        self.date_time = date_time
        self.temperature = temperature
        self.humidity = humidity
        self.weather_description = weather_description
        self._ret_stat_dic = {}  # private but not protected with __

    @property
    def ret_stat_dic(self):
        return self._ret_stat_dic

    @ret_stat_dic.setter
    def ret_stat_dic(self, value):
        # Add any validation or logic here
        self._ret_stat_dic = value


    def __str__(self):
        # When you call print(obj) or str(obj)
        # let the user know what is the output if just call the
        return f"Date & Time: {self.date_time}\nTemperature: {self.temperature:.2f}°C\nWeather: {self.weather_description}\n{'-' * 20}"

    def serializedata(self):
        """Serialize the data to a dictionary"""

        return {
            "date time": self.date_time,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "description":  self.weather_description
        }