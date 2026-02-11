# Task 2: Stock Portfolio Tracker
# CodeAlpha Internship Task

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

portfolio = {}
total_value = 0

print("📈 Welcome to Stock Portfolio Tracker")
print("\nAvailable Stocks & Prices:")
for stock, price in stock_prices.items():
    print(f"{stock} : ₹{price}")

n = int(input("\nHow many different stocks do you want to invest in? "))

for i in range(n):
    stock_name = input("\nEnter stock name: ").upper()
    
    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        investment = stock_prices[stock_name] * quantity
        portfolio[stock_name] = (quantity, investment)
        total_value += investment
    else:
        print("❌ Stock not available! Skipping...")

print("\n📊 Portfolio Summary")
print("-" * 30)

for stock, data in portfolio.items():
    print(f"{stock} | Quantity: {data[0]} | Value: ₹{data[1]}")

print("-" * 30)
print(f"💰 Total Portfolio Value: ₹{total_value}")

# Optional file saving
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":
    # Save as TXT
    with open("portfolio.txt", "w" ,encoding="utf-8") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-" * 30 + "\n")
        for stock, data in portfolio.items():
            file.write(f"{stock} | Qty: {data[0]} | Value: ₹{data[1]}\n")
        file.write(f"\nTotal Value: ₹{total_value}")

    # Save as CSV
    with open("portfolio_summary.csv", "w") as file:
        file.write("Stock,Quantity,Value\n")
        for stock, data in portfolio.items():
            file.write(f"{stock},{data[0]},{data[1]}\n")
        file.write(f"Total,,{total_value}")

    print("✅ Portfolio saved successfully!")

print("\nThank you for using Stock Portfolio Tracker 🚀")