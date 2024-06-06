class Deserializer_Factory:
    @staticmethod
    def from_raw_data(raw_data):
    # Deserialization logic for raw data
        st_all = ""  # Initialize st_all before the loop

        Deserializer_Factory.get_citytime(raw_data['city'])  # need to check
        for forecast_data in raw_data:
            st_all += Deserializer_Factory.print_forecastdata(forecast_data)
        return st_all
            # Initiate results structure, current dont use it. could be saved to DB later on
           #WeatherForecast(dt, temp, humidity, weather_description)

    @staticmethod
    def from_cached_data(cached_data: dict):
    # Deserialization logic for cached data
        pass

    @staticmethod
    def handle_error(error_data: dict):
    # Deserialization logic for error data

        return {
            "date time": "",
            "temperature": "",
            "humidity": "",
            "description":"" #self.weather_description
        }
    @staticmethod
    def create_deserialized_object(data):
        dict = data['RawData']
        if data['Failure'] is None and data['Fromcache']:
            return Deserializer_Factory.from_raw_data(dict)
        elif data['Failure'] is None and not data['Fromcache']:
            return Deserializer_Factory.from_raw_data(dict)
        elif data['Failure'] is not None:
            return Deserializer_Factory.from_raw_data(dict)

    @staticmethod
    def print_forecastdata(forecast_data):
        dt = forecast_data['dt_txt']
        temp = forecast_data['main']['temp']  # Units are metric: Celsius
        humidity = forecast_data['main']['humidity']  # Units are metric: Celsius
        weather_description = forecast_data['weather'][0]['description']
        st = (f"Date & Time: {dt}\n"
              f"Temperature: {temp:.2f}°C\n"
              f"Humidity: {humidity:.2f}\n"
              f"Weather: {weather_description}\n"
              f"{'-' * 20}")

        return st

    @staticmethod
    def get_citytime(city_name):
        """Need toi understand if i want to concatnate it to st _all"""
        # timenow = datetime.datetime.now()
        # formatted_time = timenow.strftime("%Y-%m-%d %H:%M:%S")  # Custom format without "T"
        # current_timeTZ = get_current_time_by_city(cityName)
        # formatted_time = timenow.strftime("%Y-%m-%d %H:%M:%S")  # Custom format without "T"
        # return "The current time is: " + formatted_time + ".  " + current_timeTZ
        pass



