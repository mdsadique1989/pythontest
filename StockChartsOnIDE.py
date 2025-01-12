import yfinance as yf
import matplotlib.pyplot as plt

# Prompting user for the share name
STK = input("Enter share name: ")

# Define periods and corresponding titles
periods = {
    "1d": "1 Day",
    "7d": "7 Days",
    "1mo": "1 Month",
    "6mo": "6 Months",
    "1y": "1 Year",
    "5y": "5 Years",
    "max": "Lifetime"
}

for period, title in periods.items():
    # Fetch historical market data
    data = yf.Ticker(STK).history(period=period)

    # Plotting the closing price
    plt.figure(figsize=(10, 6))
    plt.plot(data['Close'], label='Close Price')
    plt.title(f'{STK} - {title} Price Chart')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    # Display the chart
    plt.show()
