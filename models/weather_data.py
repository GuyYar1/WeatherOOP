from models.cache import Cachebase
from models.Deserilaized import Deserializer_Factory as module


class WeatherData(Cachebase):
    """This file contains the data model. """
    def __init__(self, date_time=None, temperature=None, humidity=None, weather_description=None):
        super().__init__()  # initiate base class cache
        # instance attributes
        self.date_time = date_time
        self.temperature = temperature
        self.humidity = humidity
        self.weather_description = weather_description
        self._ret_stat_dic = {}  # private but not protected with __
        self.dict_whole = {"aggrtext": "", "dataplot": {}}

    @property
    def ret_stat_dic(self):
        return self._ret_stat_dic

    @ret_stat_dic.setter
    def ret_stat_dic(self, value):
        # Add any validation or logic here
        self._ret_stat_dic = value


    def __str__(self):
        # When you call # print(obj) or str(obj)
        # let the user know what is the output if just call the
        return (f"Date & Time: {self.date_time}\nTemperature: {self.temperature:.2f}°C\nWeather: "
                f"{self.weather_description}\n{'-' * 20}")


    def serializedata(self):
        """Serialize the data to a dictionary"""
        dictt = self.ret_stat_dic
        self.dict_whole["aggrtext"] = module.DeserializerFactory.create_deserialized_object(dictt)
        self.dict_whole["dataplot"] = module.DeserializerFactory.create_plot_data(dictt)
        return self.dict_whole
