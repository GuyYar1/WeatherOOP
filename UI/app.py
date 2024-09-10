import sys
import os
import pdb

def support_abs_sys_path():
    # Get the absolute path of the project root
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    # Add the project root to Python's search path
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

support_abs_sys_path()

# Now you can use absolute imports
from services.Weather_Service_Printer import WeatherServicePrinter  ##..services
import streamlit as st
from services.plot_data import *
from services import plot_data
from menu import menu
from UI.pages import *


import pdb  # debug on run mode , good for streamlit running
# pdb.set_trace()
# How to run: open powershell type be on the root : streamlit run UI/app.py



def main():
    user_selection_option()
    menu()  # Render the dynamic menu!

    main_bg_url = "https://th.bing.com/th/id/OIP.IJRXaAJEEXBsJ5L26O4b8QAAAA?rs=1&pid=ImgDetMain"  # Replace with your image URL
    method_name(main_bg_url)

    # Program forcastweather
    st.title('                          Weather Forecast App                                                      ')
    text = "OOP Design {patterns,classes,Persistence Cache,Queue,Events,Encryption,serializers'}"
    st.markdown(f'<h1 style="font-size: 12pt;">{text}</h1>', unsafe_allow_html=True)
    city = st.text_input('Enter city name', 'Springfield')
    country = st.text_input('Enter country code (optional)', 'US')
    state = st.text_input('Enter state code (optional)', 'IL')

    if st.button('Get Weather'):
        weather_srv_obj = WeatherServicePrinter()
        weather_srv_obj.get_all_forcast(city, country, state)
        weather_srv_obj.print_data()

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


def method_name(main_bg_url):
    st.markdown(f"""
        <style>
            reportview-container {{
                background: url("{main_bg_url}");
            }}
        </style>
    """, unsafe_allow_html=True)


def user_selection_option():
    # Initialize st.session_state.role to None
    if "role" not in st.session_state:
        st.session_state.role = None
    # Retrieve the role from Session State to initialize the widget
    st.session_state._role = st.session_state.role
    # Selectbox to choose role
    st.selectbox(
        "Select your role:",
        [None, "user", "admin", "super-admin"],
        key="_role",
        on_change=set_role,
    )


def set_role():
    # Callback function to save the role selection to Session State
    st.session_state.role = st.session_state._role



if __name__ == "__main__":
    main()  # # Run the  main function
