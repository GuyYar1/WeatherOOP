import streamlit as st
from services.weather_service_printer import WeatherServicePrinter as serv
from services.queue_manager import Queue_manager

# How to run: open powershell type: streamlit run app.py

def main():
    st.title('Weather Forecast App')
    city = st.text_input('Enter city name', 'London')
    country = st.text_input('Enter country code (optional)', '')

    state = st.text_input('Enter state code (optional)', '')

    if st.button('Get Weather'):
        weather_obj = serv()
        weather_obj.get_all_forcast(city, country, state)
        weather_obj.print_data()

        while True:

            strprint = weather_obj.queue_m.consumer(weather_obj.queue_m)
            st.write(strprint)
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


if __name__ == '__main__':
    main()
