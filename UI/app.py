import sys
import os
import pandas as pd
import pdb

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
# import pdb  # debug on run mode , good for streamlit running
# pdb.set_trace()
# How to run: open powershell type be on the root : streamlit run UI/app.py

async def main():
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
        breakpoint()
        df = await Plot_PerDay_UserSlection()

        # Plotting the line chart
        st.line_chart(df.set_index('Date'))

        if next_item == "No other Item, all is dequeued":
            st.write(next_item)
            # break
        elif "The current time is" in next_item:
            # There is data
            st.write(next_item)
            st.write("-" * 20)
        else:
            st.write('Failed to retrieve weather data.')
        #asyncio.current_task().cancel()  # Cancel the current task
        ## print(sys.path)
        #st.write(sys.path)

        # except asyncio.CancelledError:
            # # break
    # else:
    #     st.write('Failed to retrieve weather data.')
    #     # async for strprint in queue_manager.consumer(): Yield not return
    #     st.write("-" * 20)
    # Clear the task after processing
    #asyncio.current_task().cancel()  # Cancel the current task


async def Plot_PerDay_UserSlection():
    data = {
        'Date': ['2024-06-17', '2024-06-18', '2024-06-19'],
        'Temperature': [22, 24, 21],
        'Humidity': [60, 65, 55]
    }
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])  # Ensure the Date column is in datetime format
    return df


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())  # # Run the async main function
