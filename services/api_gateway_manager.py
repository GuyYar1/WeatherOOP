from utils import EncodingUtils
from utils.EncodingUtils import extract_api_key
from utils.IpNetUtil import check_internet
from models.weather_data import WeatherData
from models.cache import *
import requests


class ApiGatewayManager:
    def __init__(self, model_weather: WeatherData, city_name: str, country_code: str = None):
        self.model_weather = model_weather
        self.city_name = city_name
        self.country_code = country_code
        # option to add state code.

    def get_weatherbycity(self, model_weather: WeatherData, city_name: str, country_code: str = None):
        """
             Pure Function, save data to a list of dictionaries uses:
                                Call 5 day / 3 hour forecast data at:
                                            https://openweathermap.org/forecast5#name5
             get_weather by city:  gets(cityName: str, country_code: str )
             :param model_weather:
                   """
        cache_key = model_weather.get_cache_key(city_name, country_code)
        self.print_timesinfo(city_name) # Implement but not here.

        if not (model_weather.is_cache_valid(cache_key)):
            # if the cache doesnt have this data or the data retrieved more than 2 hours, consider old data

            api_url = "http://api.openweathermap.org/data/2.5/forecast"
            units = "metric"
            appidsufiix = EncodingUtils.readprofile("file.env")
            appid = extract_api_key(appidsufiix)
            # appid = "8fc9d67f835721026f13442e85c59884"  # EncodingUtils.encode_to_base64 doesnt support
            city = city_name
            country = country_code

            if not check_internet():
                print(f"check your internet connection - seems that you have an issue\n")
                print(f"Your query is not in the mem cache or file cache, fix the issue and re run")
                exit()

            if country is None:
                response = requests.get(api_url, params={"q": city, "units": units, "appid": appid})
            # api.openweathermap.org/data/2.5/forecast?q=London&units=metric&appid=8fc9d67f835721026f13442e85c59884
            else:
                response = requests.get(api_url, params={"q": city + "," + country, "units": units, "appid": appid})
            print("Data retrieved by restfull API gateway ...")
            # # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()
                # Display the data
                city = data['city']['name']
                country = data['city']['country']
                print(f"Weather Forecast for {city}, {country}. Please ensure that this is what you requested \n")

                # Iterate through the forecast list and print details
                # forecast_list = []

                for forecast_data in data['list']:
                    #dt, humidity, temp, weather_description = self.print_forecastdata(forecast_data)
                    dt, humidity, temp, weather_description = [5, 5, 5, 5] # temp refactor
                    # Initiate results structure, current dont use it. could be saved to DB later on
                    model_weather = WeatherData(dt, temp, humidity, weather_description)

                # save to cache
                model_weather.set_cache(cache_key, data['list'])
                return data['list']

                # Now forecast_list contains a list of WeatherForecast objects
            else:
                print("Failed to retrieve data")
                return None
        else:
            #  the data retrived by caching
            print("Data retrieved by mem cache or file cache")
            cache_data = model_weather.get_from_cache(cache_key)
            for forecast_cache_data in cache_data:
                self.print_forecastdata(forecast_cache_data) # Refactor not here
            return cache_data

    def print_forecastdata(self, forecast_data):
        pass

    def print_timesinfo(self, cityName):
        pass
