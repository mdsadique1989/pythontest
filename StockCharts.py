import yfinance as yf
import mplfinance as mpf

# Corrected input statement
ticker = input("Enter the stock name: ")

# Corrected download function with proper syntax
df = yf.download(ticker, start='2023-08-01', end='2024-09-01')

# Corrected plot function with proper formatting
mpf.plot(df, type='candle', style='charles',
         title=f'{ticker} Candlestick Chart', ylabel='Price')