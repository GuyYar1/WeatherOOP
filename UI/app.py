import sys
import os
# import pdb


def support_abs_sys_path():
    # Get the absolute path of the project root
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    # Add the project root to Python's search path
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

support_abs_sys_path()

# Now you can use absolute imports
from services.WeatherServicePrinter import WeatherServicePrinter  ##..services
import streamlit as st
from services.plot_data import *
from services import plot_data
import pdb  # debug on run mode , good for streamlit running
# pdb.set_trace()
# How to run: open powershell type be on the root : streamlit run UI/app.py

def main():
    #breakpoint()
    st.title('                          Weather Forecast App                                                      ')
    text = "OOP Design {patterns,classes,Persistence Cache,Queue,Events,Encryption,serializers'}"
    st.markdown(f'<h1 style="font-size: 12pt;">{text}</h1>', unsafe_allow_html=True)
    city = st.text_input('Enter city name', 'Springfield')
    country = st.text_input('Enter country code (optional)', 'US')
    state = st.text_input('Enter state code (optional)', 'IL')

    if st.button('Get Weather'):
        weather_srv_obj = WeatherServicePrinter()
        #breakpoint()
        weather_srv_obj.get_all_forcast(city, country, state)
        weather_srv_obj.print_data()

        #while True:
        #try:
        next_item = weather_srv_obj.get_from_queue()
        #  #next_item format =>  {"textarea": str, "dict plot": dictplot --streamlit}

        df = plot_data.Plot_data1.plot_per_day_user_section(next_item["dataplot"])

        # Create a DataFrame for plotting
        df = pd.DataFrame(df)

        # Set 'Date' as the index for the DataFrame
        df.set_index('Date', inplace=True)

        # Create a bar chart with dates on the x-axis
        st.bar_chart(df)

        if next_item["aggrtext"] == "No other Item, all is dequeued":
            st.write(next_item["aggrtext"])
        elif "The current time is" in next_item["aggrtext"]:
            # There is data
            st.write(next_item["aggrtext"])
            st.write("-" * 20)
        else:
            st.write('Failed to retrieve weather data.')


if __name__ == "__main__":
    main()  # # Run the  main function
