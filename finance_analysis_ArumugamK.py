# Importing necessary libraries
from ta.trend import CCIIndicator
from ta.trend import SMAIndicator
from ta.volatility import BollingerBands
import pandas as pd
from yahooquery import Ticker

# Adding Space
print("\n" + "-"*50 + "\n")

# 1. Scraping Data from Yahoo Finance (From Jan 1, 2023 to Dec 7, 2023)
print("Scraped data from Yahoo Finance From Jan 1, 2023 to Dec 7, 2023")

# Defining the ticker symbol for EUR/INR
ticker = 'EURINR=X'

# Defining the date range
start_date = '2023-01-01'
end_date = '2023-12-07'

# Fetching historical data using yahooquery
eur_inr_ticker = Ticker(ticker)
data = eur_inr_ticker.history(start=start_date, end=end_date)

# Saving the data to a CSV file
data.to_csv('historical_data.csv')

# Displaying the entire DataFrame
print(data)

# Adding Space
print("\n" + "-"*50 + "\n")






# 2. Scraping Data from Yahoo Finance (From Jan 1, 2023 to Dec 14, 2023)
print("2. Scraped data from Yahoo Finance From Jan 1, 2023 to Dec 14, 2023")

# Defining the ticker symbol for EUR/INR
ticker = 'EURINR=X'

# Defining the date range
start_date = '2023-01-01'
end_date = '2023-12-14'

# Fetching historical data using yahooquery
eur_inr_ticker = Ticker(ticker)
data = eur_inr_ticker.history(start=start_date, end=end_date)

# Saving the data to a CSV file
data.to_csv('historical_data.csv')

# Displaying the entire DataFrame
print(data)

# Adding Space
print("\n" + "-"*50 + "\n")




# 3. Conducting Technical Analysis - Moving Average
print("Conducted technical analysis - Moving Average")

# Loading the scraped data
data_from_dec_7 = pd.read_csv('historical_data.csv')

# Filtering data for dates from December 7, 2023, to December 14, 2023
data_from_dec_7 = data_from_dec_7[(data_from_dec_7['date'] >= '2023-12-07') & (data_from_dec_7['date'] <= '2023-12-14')]

# Converting the 'date' column to datetime format
data_from_dec_7['date'] = pd.to_datetime(data_from_dec_7['date'])

# Sorting the DataFrame based on the 'date' column
data_from_dec_7 = data_from_dec_7.sort_values(by='date')

# Calculating Moving Average for one day and one week
indicator_sma_1day = SMAIndicator(close=data_from_dec_7['close'], window=1)
data_from_dec_7['one day'] = indicator_sma_1day.sma_indicator()

indicator_sma_7days = SMAIndicator(close=data_from_dec_7['close'], window=7)
data_from_dec_7['one week'] = indicator_sma_7days.sma_indicator()

# Displaying the rows of the technical analysis data
print(data_from_dec_7[['date', 'close', 'one day', 'one week']])

# Adding Space
print("\n" + "-"*50 + "\n")



# 4. Conducting Technical Analysis - Bollinger Bands
print("Conducted technical analysis - Bollinger Bands")

# Loading the scraped data
data = pd.read_csv('historical_data.csv')

# Filtering data from December 7, 2023, to December 14, 2023
data_from_dec_7 = data[(data['date'] >= '2023-12-07') & (data['date'] <= '2023-12-14')]

# Sorting the DataFrame based on the 'date' column
data_from_dec_7 = data_from_dec_7.sort_values(by='date')

# Calculating Bollinger Bands
bb = BollingerBands(close=data_from_dec_7['close'], window=20, window_dev=2)

# Adding Bollinger Bands to the DataFrame
data_from_dec_7['one day'] = bb.bollinger_hband()
data_from_dec_7['one week'] = bb.bollinger_lband()

# Displaying the rows of the DataFrame with new columns
print(data_from_dec_7[['date', 'close', 'one day', 'one week']])

# Adding Space
print("\n" + "-"*50 + "\n")



# 5. Conducting Technical Analysis - Commodity Channel Index
print("Conducted technical analysis - Commodity Channel Index")

# Loading the scraped data
data = pd.read_csv('historical_data.csv')

# Filtering data from December 7, 2023, to December 14, 2023
data_from_dec_7 = data[(data['date'] >= '2023-12-07') & (data['date'] <= '2023-12-14')]

# Sorting the DataFrame based on the 'date' column
data_from_dec_7 = data_from_dec_7.sort_values(by='date')

# Adding high and low columns
data_from_dec_7['high'] = data_from_dec_7['high']
data_from_dec_7['low'] = data_from_dec_7['low']

# Calculating Commodity Channel Index (CCI) for one day and one week
cci_1day = CCIIndicator(close=data_from_dec_7['close'], high=data_from_dec_7['high'], low=data_from_dec_7['low'], window=1)
data_from_dec_7['one day'] = cci_1day.cci()

cci_1week = CCIIndicator(close=data_from_dec_7['close'], high=data_from_dec_7['high'], low=data_from_dec_7['low'], window=7)
data_from_dec_7['one week'] = cci_1week.cci()

# Displaying the rows of the DataFrame with new columns
print(data_from_dec_7[['date', 'close', 'one day', 'one week']])

# Adding Space
print("\n" + "-"*50 + "\n")




# 6. Decision Making - Generate Signals
print("Decision Making - Generated Signal")

# Function to generate signals
def generate_signals(row):
    if row['one day'] > row['one week'] and row['close'] < row['one day']:
        return 'BUY'
    elif row['one day'] < row['one week'] and row['close'] > row['one week']:
        return 'SELL'
    else:
        return 'NEUTRAL'

# Applying
data_from_dec_7['signal'] = data_from_dec_7.apply(generate_signals, axis=1)

# Displaying the result
print(data_from_dec_7[['date', 'close', 'one day', 'one week', 'signal']])

# Adding Space
print("\n" + "-"*50 + "\n")



