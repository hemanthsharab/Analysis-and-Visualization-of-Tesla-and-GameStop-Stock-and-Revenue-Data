import yfinance as yf

# Download Tesla stock data
tesla_data = yf.Ticker("TSLA").history(period="max")

# Reset the index
tesla_data.reset_index(inplace=True)

# Display the first five rows
print(tesla_data.head())
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Scrape Tesla revenue data
url = "https://example.com/tesla-revenue"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract data and create a DataFrame
tesla_revenue_data = []
for row in soup.find_all("tr"):
    cols = row.find_all("td")
    if cols:
        tesla_revenue_data.append([col.text.strip() for col in cols])

# Convert to DataFrame
tesla_revenue = pd.DataFrame(tesla_revenue_data, columns=["Date", "Revenue"])

# Display the last five rows
print(tesla_revenue.tail())
# Download GameStop stock data
gme_data = yf.Ticker("GME").history(period="max")

# Reset the index
gme_data.reset_index(inplace=True)

# Display the first five rows
print(gme_data.head())

# Scrape GameStop revenue data
url = "https://example.com/gme-revenue"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract data and create a DataFrame
gme_revenue_data = []
for row in soup.find_all("tr"):
    cols = row.find_all("td")
    if cols:
        gme_revenue_data.append([col.text.strip() for col in cols])

# Convert to DataFrame
gme_revenue = pd.DataFrame(gme_revenue_data, columns=["Date", "Revenue"])

# Display the last five rows
print(gme_revenue.tail())
import matplotlib.pyplot as plt

# Function to make a graph
def make_graph(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data["Date"], data["Close"], label="Close Price")
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.legend()
    plt.grid(True)
    plt.show()

# Plot Tesla stock data
make_graph(tesla_data, "Tesla Stock Price Over Time")
# Plot GameStop stock data
make_graph(gme_data, "GameStop Stock Price Over Time")
