# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "MSFT": 310,
    "AMZN": 145
}

# Step 1: Take user input
portfolio = {}  # Dictionary to store user input
print("Enter stock symbol and quantity (type 'done' to finish):")

while True:
    stock = input("Stock Symbol (e.g., AAPL): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print(f"'{stock}' not in available stocks. Try again.")
        continue
    try:
        quantity = int(input(f"Quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

# Step 2: Calculate total investment
total_investment = 0
print("\n=== Portfolio Summary ===")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_investment += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Step 3: Optionally save to CSV
save = input("\nDo you want to save the result to a CSV file? (yes/no): ").lower()
if save == 'yes':
    import csv
    with open("portfolio_summary.csv", mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            writer.writerow([stock, qty, price, qty * price])
        writer.writerow(["Total", "", "", total_investment])
    print("Portfolio saved to portfolio_summary.csv")
