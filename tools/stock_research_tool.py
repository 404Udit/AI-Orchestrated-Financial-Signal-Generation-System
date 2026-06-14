import yfinance as yf
import pandas as pd
from crewai.tools import tool

@tool("Live Stock Information Tool")
def get_stock_data(stock_symbol: str, end_date: str = None) -> dict:
    """
    Analyze historical stock data up to a specified date and generate a structured
    market condition report for downstream decision-making agents.

    Description:
        This task instructs the Financial Market Analyst agent to:
        - Use the Live Stock Information Tool to retrieve stock data
        up to the provided end_date.
        - Interpret key technical indicators such as trend direction,
        volatility, and moving averages.
        - Summarize the current market condition in structured JSON format.

    Inputs:
        stock (str): The ticker symbol of the stock (e.g., AAPL, TSLA, MSFT).
        end_date (str, optional): Historical cutoff date (YYYY-MM-DD)
                                for backtesting simulations.

    Expected Output:
        dict: A structured JSON object containing:
            - stock (str): Stock ticker symbol
            - current_price (float): Closing price on end_date
            - trend (str): Bullish or Bearish trend indication
            - volatility (float): Recent return volatility
            - market_summary (str): Interpretation of market condition
    """

    stock = yf.Ticker(stock_symbol)

    if end_date:
        hist = stock.history(end=end_date, period="90d")
    else:
        hist = stock.history(period="90d")

    if hist.empty:
        return {"error": "Invalid stock symbol"}

    current_price = hist["Close"].iloc[-1]
    open_price = hist["Open"].iloc[-1]

    change_percent = ((current_price - open_price) / open_price) * 100

    sma_7 = hist["Close"].rolling(7).mean().iloc[-1]
    sma_30 = hist["Close"].rolling(30).mean().iloc[-1]
    volatility = hist["Close"].pct_change().std()

    trend = "Bullish" if sma_7 > sma_30 else "Bearish"

    return {
        "stock": stock_symbol.upper(),
        "current_price": round(current_price, 2),
        "change_percent": round(change_percent, 2),
        "sma_7": round(sma_7, 2),
        "sma_30": round(sma_30, 2),
        "trend": trend,
        "volatility": round(volatility, 4)
    }

