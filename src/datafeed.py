import yfinance as yf
from joblib import Memory

memory = Memory(location="data/")


@memory.cache
def get_data(end_dt):
    """"""
    # Define the tickers
    tickers = ["^GSPC", "AAPL", "CVX", "DAL", "GM", "GS", 
               "JPM", "LUV", "MSFT", "SPY", "TSLA", "XOM"]

    # Download stock price data
    res = yf.download(tickers, start="2010-01-01", end=end_dt)\
        ['Adj Close']\
        .rename(columns={"^GSPC": "SP500"})

    return res
