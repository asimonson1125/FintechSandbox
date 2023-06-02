import requests
import matplotlib.pyplot as plt
import plotter
from envs import apikey


def get_stock_price_history(ticker, start_date, end_date, frequencyType=None, frequency=None):
    """
    Get the historical stock price data for a given ticker without yfinance.

    Args:
      ticker: The stock ticker symbol.
      start_date: The start date of the historical data.
      end_date: The end date of the historical data.

    Returns:
      A pandas DataFrame containing the historical stock price data.
    """

    # Get the stock price data from the Quandl API.
    url = f"https://api.tdameritrade.com/v1/marketdata/{ticker}/pricehistory?apikey={apikey}&endDate={end_date}&startDate={start_date}&needExtendedHoursData=false"
    if not frequencyType == None:
        url += f"&frequencyType={frequencyType}"
    if not frequency == None:
        url += f"&frequency={frequency}"
    response = requests.get(url).json()

    # Return the DataFrame.
    return response


# Get the historical stock price data for Apple from 2020-01-01 to 2023-06-01.
data = get_stock_price_history(
    "AAPL", start_date="1641013200000", end_date="1685731425617")

ax = plotter.candle_plot(data['candles'][:130])

# Save the figure
plt.savefig('candlestick_chart.png')

