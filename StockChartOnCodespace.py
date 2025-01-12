import yfinance as yf
import matplotlib.pyplot as plt

# Prompting user for the share name
STK = input("Enter share name: ")

# Define periods and corresponding titles
periods = {
    "1d": "1 Day",
    "5d": "5 Days",
    "1mo": "1 Month",
    "3mo": "3 Months",
    "6mo": "6 Months",
    "ytd": "YTD",
    "5y": "5 Years",
    "10y": "10 Years",
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

    # Save the chart as an image
    file_name = f'{STK}_{title.replace(" ", "_").lower()}.png'
    plt.savefig(file_name)
    print(f"Chart saved as {file_name}")

    # Clear the figure for the next plot
    plt.close()