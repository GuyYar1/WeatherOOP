import pandas as pd


class Plot_data1:
    @staticmethod
    def plot_per_day_user_section(dictoplot, mod=1):

        # data = {
        #     'Date': ['2024-06-17', '2024-06-18', '2024-06-19'],
        #     'Temperature': [22, 24, 21],
        #     'Humidity': [60, 65, 55]
        # }
        # remove from here to seperate file
        df = pd.DataFrame(dictoplot)
        df['Date'] = pd.to_datetime(df['Date'])  # Ensure the Date column is in datetime format

        # Convert date strings to datetime objects
        df['Date'] = pd.to_datetime(df['Date'])

        # add option to filter the data with modulo current 1
        # Calculate modulo 4 for Temperature and Humidity
        selected_data = {
            key: [value % mod if isinstance(value, int) else value for value in values]
            for key, values in df.items()}

        return selected_data

