import sys
import os

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
# import pdb
# pdb.set_trace()
# How to run: open powershell type be on the root : streamlit run UI/app.py

async def main():
    #breakpoint()
    st.title('Weather Forecast App')
    city = st.text_input('Enter city name', 'Springfield')
    country = st.text_input('Enter country code (optional)', 'US')
    state = st.text_input('Enter state code (optional)', 'IL')


    if st.button('Get Weather'):
        weather_srv_obj = WeatherServicePrinter()
        # breakpoint()
        weather_srv_obj.get_all_forcast(city, country, state)
        await weather_srv_obj.print_data()

        while True:
            try:
                next_item = await weather_srv_obj.get_from_queue()
                st.write(next_item)
                st.write("-" * 20)
                # Clear the task after processing
                asyncio.current_task().cancel()  # Cancel the current task
                ## print(sys.path)
                #st.write(sys.path)
            except asyncio.CancelledError:
                break
    else:
        st.write('Failed to retrieve weather data.')
        # async for strprint in queue_manager.consumer(): Yield not return
        st.write("-" * 20)
        # Clear the task after processing
        asyncio.current_task().cancel()  # Cancel the current task


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())  # # Run the async main function
