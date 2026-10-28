
import csv
import os

# Sample stock prices (current prices for practice)
stock_prices = {
    "AAPL": 230.00,
    "MSFT": 510.00,
    "GOOGL": 250.00,
    "AMZN": 220.00,
    "NVDA": 180.00
}

portfolio = {}

print("=" * 50)
print("       STOCK PORTFOLIO PERFORMANCE TRACKER")
print("=" * 50)

while True:
    ticker = input(
        "\nEnter stock ticker (or 'done' to finish): "
    ).strip().upper()

    if ticker == "DONE":
        break

    if not ticker.isalpha():
        print("Invalid ticker. Please enter letters only.")
        continue

    try:
        buy_price = float(input("Enter purchase price per share: "))
        quantity = int(input("Enter number of shares: "))

        if buy_price <= 0 or quantity <= 0:
            print("Price and quantity must be positive.")
            continue

    except ValueError:
        print("Please enter a valid numeric price and quantity.")
        continue

    # Use sample price if available
    if ticker in stock_prices:
        current_price = stock_prices[ticker]
    else:
        current_price = float(
            input("Current price not found. Enter current price: ")
        )

        if current_price <= 0:
            print("Current price must be positive.")
            continue

    # Store position in dictionary
    if ticker in portfolio:
        print("This ticker is already in your portfolio.")
        print("Please finish and restart to enter it separately.")
        continue

    portfolio[ticker] = {
        "buy_price": buy_price,
        "quantity": quantity,
        "current_price": current_price
    }

if not portfolio:
    print("\nNo stocks were entered. Exiting program.")
    raise SystemExit

total_invested = 0
total_market_value = 0

print("\n" + "=" * 75)
print("PORTFOLIO SUMMARY")
print("=" * 75)

print(
    f"{'Ticker':<10}"
    f"{'Quantity':<10}"
    f"{'Invested':<15}"
    f"{'Current Value':<16}"
    f"{'Gain/Loss %':<12}"
)

print("-" * 75)

# Write summary to CSV file
with open(
    "portfolio_summary.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Ticker",
        "Buy Price",
        "Quantity",
        "Current Price",
        "Total Invested",
        "Current Value",
        "Gain/Loss",
        "Gain/Loss Percentage"
    ])

    for ticker, details in portfolio.items():
        buy_price = details["buy_price"]
        quantity = details["quantity"]
        current_price = details["current_price"]

        invested = buy_price * quantity
        current_value = current_price * quantity
        gain_loss = current_value - invested
        percentage = (gain_loss / invested) * 100

        total_invested += invested
        total_market_value += current_value

        print(
            f"{ticker:<10}"
            f"{quantity:<10}"
            f"${invested:<14.2f}"
            f"${current_value:<15.2f}"
            f"{percentage:>9.2f}%"
        )

        writer.writerow([
            ticker,
            f"{buy_price:.2f}",
            quantity,
            f"{current_price:.2f}",
            f"{invested:.2f}",
            f"{current_value:.2f}",
            f"{gain_loss:.2f}",
            f"{percentage:.2f}"
        ])

total_gain_loss = total_market_value - total_invested

if total_invested > 0:
    total_percentage = (total_gain_loss / total_invested) * 100
else:
    total_percentage = 0

print("-" * 75)
print(f"Total Invested:      ${total_invested:.2f}")
print(f"Total Market Value:  ${total_market_value:.2f}")
print(f"Total Gain/Loss:     ${total_gain_loss:.2f}")
print(f"Portfolio Return:    {total_percentage:.2f}%")
print("=" * 75)

print("\nSummary saved to portfolio_summary.csv")
