from utils import EncodingUtils
from utils.EncodingUtils import extract_api_key
from utils.IpNetUtil import check_internet
from models.weather_data import WeatherData
from models.cache import *
import requests


def api_serve():
    """internal this is a function and not a method.  called from the class """
    api_url = "http://api.openweathermap.org/data/2.5/forecast"
    units = "metric"
    appidsufiix = EncodingUtils.readprofile("file.env")
    appid = extract_api_key(appidsufiix)
    return api_url, appid, units


class ApiGatewayManager:
    def __init__(self, model_weather: WeatherData, city_name: str, country_code: str = None):
        self.model_weather = model_weather
        self.city_name = city_name          # requested
        self.country_code = country_code    # requested
        # option to add state code.

    def get_weatherbycity(self, model_weather: WeatherData, city_name: str, country_code: str = None):
        """
             Call 5 day / 3 hour forecast data at:    https://openweathermap.org/forecast5#name5
             get_weather by city:  gets(model_weather: WeatherData ,cityName: str, country_code: str )
             param model_weather, set in the WeatherData ret_stat_dic:
             retstat =
                        Failure                    : None | Connection | response.status_code
                        RetCity                    : None | ret_city
                        RetCountry                 : None | ret_country
                        RawData                    : None | data
                        Fromcache                  : None | 1 | 0
        """
        cache_key = model_weather.get_cache_key(city_name, country_code)

        self.print_timesinfo(city_name) # Implement but not here. ##$REFACTOR##$

        if not (model_weather.is_cache_valid(cache_key)):
            # if the cache doesnt have this data or the data retrieved more than 2 hours, consider old data

            api_url, appid, units = api_serve()
            # appid = "8fc9d67f835721026f13442e85c59884"  # EncodingUtils.encode_to_base64 doesnt support

            if not check_internet():
                # print(f"check your internet connection - seems that you have an issue\n")
                # print(f"Your query is not in the mem cache or file cache, fix the issue and re run")
                self.model_weather.ret_stat_dic = {"Failure": "Connection","RetCity": None ,"RetCountry": None ,
                                                   "RawData": None ,"Fromcache": None}
                exit()  # #OUT

            if self.country_code is None:
                response = requests.get(api_url, params={"q": self.city_name, "units": units, "appid": appid})
            # api.openweathermap.org/data/2.5/forecast?q=London&units=metric&appid=8fc9d67f835721026f13442e85c59884
            else:
                response = requests.get(api_url, params={"q": self.city_name + "," + self.country_code,
                                                         "units": units, "appid": appid})
            print("Data retrieved by restfull API gateway ...")
            # # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()
                # Display the data
                ret_city = data['city']['name']
                ret_country = data['city']['country']
                self.model_weather.ret_stat_dic = {"Failure": "None", "RetCity": ret_city, "RetCountry": ret_country,
                                                   "RawData": data, "Fromcache": False}  # setter
                print(f"Weather Forecast for {ret_city}, {ret_country}. Please ensure that this is what you requested \n")
                # save to cache
                model_weather.set_cache(cache_key, data['list'])
                return  # # OUT

                    # Iterate through the forecast list and print details
                    # forecast_list = []

                    #for forecast_data in data['list']:
                    #    dt, humidity, temp, weather_description = self.print_forecastdata(forecast_data)
                    #    dt, humidity, temp, weather_description = [5, 5, 5, 5]  # temp refactor
                    #    # Initiate results structure, current dont use it. could be saved to DB later on
                    #    model_weather = WeatherData(dt, temp, humidity, weather_description)

                # Now forecast_list contains a list of WeatherForecast objects
            else:
                print("Failed to retrieve data")
                self.model_weather.ret_stat_dic = {"Failure": response.status_code, "RetCity": None, "RetCountry": None,
                                                   "RawData": None, "Fromcache": None}

        else:
            #  the data retrived by caching
            print("Data retrieved by mem cache or file cache")
            cache_data = model_weather.get_from_cache(cache_key)
            # for forecast_cache_data in cache_data:
            #    self.print_forecastdata(forecast_cache_data) # Refactor not here ##$REFACTOR##$
            # return cache_data

            self.model_weather.ret_stat_dic = {"Failure": None, "RetCity": None, "RetCountry": None,
                                               "RawData": cache_data, "Fromcache": True}

    def print_forecastdata(self, forecast_data):
        pass

    def print_timesinfo(self, cityName):
        pass
