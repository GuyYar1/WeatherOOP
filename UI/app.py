import asyncio
import sys
import os

# Get the absolute path of the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the project root to Python's search path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Now you can use absolute imports
from services.WeatherServicePrinter import WeatherServicePrinter as Wea
from services.queue_manager import Queue_manager
import streamlit as st
# # from ..services.WeatherServicePrinter import WeatherServicePrinter as Wea
# # from ..services.queue_manager import Queue_manager
import pdb
# pdb.set_trace()


# How to run: open powershell type: streamlit run app.py

async def main():
    #breakpoint()
    st.title('Weather Forecast App')
    city = st.text_input('Enter city name', 'London')
    country = st.text_input('Enter country code (optional)', '')
    #breakpoint()
    state = st.text_input('Enter state code (optional)', '')

    if city is None:
        city = ""
    if country is None:
        country = ""

    if st.button('Get Weather'):
        weather_obj = Wea()
        await weather_obj.get_all_forcast(city, country, state)
        await weather_obj.print_data()

        while True:
            strprint = await Queue_manager.consumer(weather_obj.queue_manager, weather_obj.queue_manager)
            st.write(strprint)
        #print(sys.path)
        #st.write(sys.path)
            st.write("-" * 20)
                #
            # for forecast in forecast_list:
            #     dt = forecast['dt_txt']
            #     temp = forecast['main']['temp']  # Units are metric: Celsius
            #     humidity = forecast['main']['humidity']  # Units are metric: Celsius
            #     weather_description = forecast['weather'][0]['description']
            #     st.write(f"The selected city_name is: {city} in the country code: {str(country)}")
            #     st.write(weather_forecast.print_timesinfo(city, "streamlit"))
            #     st.write("-" * 20)
            #     st.write(f"Date & Time: {dt}")
            #     st.write(f"Temperature: {temp:.2f}°C")
            #     st.write(f"Humidity: {humidity:.2f}")
            #     st.write(f"Weather: {weather_description}")

    else:
        st.write('Failed to retrieve weather data.')


if __name__ == "__main__":
    asyncio.run(main())  # Run the async main function