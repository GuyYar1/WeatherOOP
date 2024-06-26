from utils.Time_Utils import *
import datetime


class DeserializerFactory:

    @staticmethod
    def create_deserialized_object(data):
        raw_data = data['RawData']
        # # from cache it filled with None and from raw data "None"
        instance = DeserializerFactory()

        if data['Failure'] is None:
            if data['Fromcache']:
                return DeserializerFactory.from_cached_data(raw_data, data.get('RetCity'))
            else:
                return DeserializerFactory.from_raw_data(raw_data, data.get('RetCity'))
        else:
            return DeserializerFactory.handle_error(data['Failure'])

    @staticmethod
    def create_plot_data(raw_data):

        data = {'Date': [], 'Temperature': [], 'Humidity': []}

        if raw_data["Failure"] is not None:
            return data  # # failure no data, check why
        else:
            if raw_data['Fromcache']:
                forecast_dict = raw_data["RawData"]
            else:
                forecast_dict = raw_data['RawData']['list']

        for forecast_data in forecast_dict:
            data['Date'].append(forecast_data['dt_txt'])
            data['Temperature'].append(forecast_data['main']['temp'])
            data['Humidity'].append(forecast_data['main']['humidity'])
        return data

    @staticmethod
    def from_raw_data(raw_data, city=None):
        st_all = ""  # Initialize st_all before the loop

        if city is not None:  # and city in raw_data:
            st_all += DeserializerFactory.get_citytime(city)

        for forecast_data in raw_data["list"]:
            st_all += DeserializerFactory.print_forecastdata(forecast_data)

        return st_all

    @staticmethod
    def from_cached_data(cached_data: dict, city=None):
        # Deserialization logic for cached data
        st_all = ""  # Initialize st_all before the loop

        if city is not None:  # and city in raw_data:
            st_all += DeserializerFactory.get_citytime(city)
        for forecast_data in cached_data:
            st_all += DeserializerFactory.print_forecastdata(forecast_data)
        return st_all

    @staticmethod
    def handle_error(error_data: dict):
        # Deserialization logic for error data
        return {
            "date time": "",
            "temperature": "",
            "humidity": "",
            "description": ""  # self.weather_description
        }

    @staticmethod
    def print_forecastdata(forecast_data):
        dt = forecast_data['dt_txt']
        temp = forecast_data['main']['temp']  # Units are metric: Celsius
        humidity = forecast_data['main']['humidity']  # Units are metric: Celsius
        weather_description = forecast_data['weather'][0]['description']

        st = (f"\n"
              f"Date & Time: {dt}\n"
              f"Temperature: {temp:.2f}°C\n"
              f"Humidity: {humidity:.2f}\n"
              f"Weather: {weather_description}\n"
              f"{'-' * 20}\n"
              )

        return st

    @staticmethod
    def get_citytime(city_name):
        """Concatenate city time information to st_all"""

        timenow = datetime.datetime.now()
        formatted_time = timenow.strftime("%Y-%m-%d %H:%M:%S")  # Custom format without "T"
        current_timeTZ = get_current_time_by_city(city_name)
        return f"The current time is: {formatted_time}.  {current_timeTZ}\n"

# import datetime
# from utils.TimeUtils import *
# import datetime
#
# class DeserializerFactory:
#     @staticmethod
#     def from_raw_data(raw_data, city=None):
#         st_all = ""  # Initialize st_all before the loop
#
#         if city and city in raw_data:
#             st_all += DeserializerFactory.get_citytime(city)
#
#         for forecast_data in raw_data:
#             st_all += DeserializerFactory.print_forecastdata(forecast_data)
#
#         return st_all
#
#     @staticmethod
#     def from_cached_data(cached_data: dict):
#         # Deserialization logic for cached data
#         pass
#
#     @staticmethod
#     def handle_error(error_data: dict):
#         # Deserialization logic for error data
#         return {
#             "date time": "",
#             "temperature": "",
#             "humidity": "",
#             "description": ""  # self.weather_description
#         }
#
#     @staticmethod
#     def create_deserialized_object(data):
#         raw_data = data['RawData']
#         if data['Failure'] is None:
#             if data['Fromcache']:
#                 breakpoint()
#                 return DeserializerFactory.from_raw_data(raw_data, data.get('RetCity'))
#             else:
#                 breakpoint()
#                 return DeserializerFactory.from_raw_data(raw_data)
#         else:
#             breakpoint()
#             return DeserializerFactory.handle_error(data['Failure'])
#
#     @staticmethod
#     def print_forecastdata(forecast_data):
#         dt = forecast_data['dt_txt']
#         temp = forecast_data['main']['temp']  # Units are metric: Celsius
#         humidity = forecast_data['main']['humidity']  # Units are metric: Celsius
#         weather_description = forecast_data['weather'][0]['description']
#
#         st = (
#             f"Date & Time: {dt}\n"
#             f"Temperature: {temp:.2f}°C\n"
#             f"Humidity: {humidity:.2f}\n"
#             f"Weather: {weather_description}\n"
#             f"{'-' * 20}\n"
#         )
#
#         return st
#
#     @staticmethod
#     def get_citytime(city_name):
#         """Concatenate city time information to st_all"""
#
#         timenow = datetime.datetime.now()
#         formatted_time = timenow.strftime("%Y-%m-%d %H:%M:%S")  # Custom format without "T"
#         current_timeTZ = get_current_time_by_city(city_name)
#         return f"The current time is: {formatted_time}.  {current_timeTZ}\n"
#

# old below delete it after testing
# class DeserializerFactory:
#     @staticmethod
#     def from_raw_data(raw_data, city):
#     # Deserialization logic for raw data
#         st_all = ""  # Initialize st_all before the loop
#
#         #city = city if city.isalpha() else "Adult"
#
#         if city.isalpha():
#             st_all += DeserializerFactory.get_citytime(raw_data[city])  # need to check
#         for forecast_data in raw_data:
#             st_all += DeserializerFactory.print_forecastdata(forecast_data)
#         return st_all
#
#     @staticmethod
#     def from_cached_data(cached_data: dict):
#     # Deserialization logic for cached data
#         pass
#
#     @staticmethod
#     def handle_error(error_data: dict):
#     # Deserialization logic for error data
#
#         return {
#             "date time": "",
#             "temperature": "",
#             "humidity": "",
#             "description":"" #self.weather_description
#         }
#     @staticmethod
#     def create_deserialized_object(data):
#         dict = data['RawData']
#         if data['Failure'] is None and data['Fromcache']:
#             return DeserializerFactory.from_raw_data(dict, data['RetCity'])
#         elif data['Failure'] is None and not data['Fromcache']:
#             return DeserializerFactory.from_raw_data(dict)
#         elif data['Failure'] is not None:
#             return DeserializerFactory.from_raw_data(dict)
#
#     @staticmethod
#     def print_forecastdata(forecast_data):
#         dt = forecast_data['dt_txt']
#         temp = forecast_data['main']['temp']  # Units are metric: Celsius
#         humidity = forecast_data['main']['humidity']  # Units are metric: Celsius
#         weather_description = forecast_data['weather'][0]['description']
#         st = (f"Date & Time: {dt}\n"
#               f"Temperature: {temp:.2f}°C\n"
#               f"Humidity: {humidity:.2f}\n"
#               f"Weather: {weather_description}\n"
#               f"{'-' * 20}")
#
#         return st
#
#     @staticmethod
#     def get_citytime(city_name):
#         """Need toi understand if i want to concatnate it to st _all"""
#
#         timenow = datetime.datetime.now()
#         formatted_time = timenow.strftime("%Y-%m-%d %H:%M:%S")  # Custom format without "T"
#         current_timeTZ = get_current_time_by_city(city_name)
#         formatted_time = timenow.strftime("%Y-%m-%d %H:%M:%S")  # Custom format without "T"
#         return "The current time is: " + formatted_time + ".  " + current_timeTZ
#
#
#
#
