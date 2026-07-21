# Stock Portfolio Tracker

stock_prices = {
    "tcs": 3500,
    "infosys": 1600,
    "reliance": 2800,
    "wipro": 550,
    "hdfcbank": 1700
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:

    stock_name = input("\nEnter Stock Name: ").lower()

    if stock_name == "done":
        break

    if stock_name in stock_prices:

        quantity = int(input("Enter Quantity: "))

        investment = stock_prices[stock_name] * quantity

        total_investment += investment

        print("Price Per Share:", stock_prices[stock_name])
        print("Investment:", investment)

    else:
        print("Stock Not Found!")

print("\nTotal Investment =", total_investment)
with open("result.txt", "w") as file:
    file.write("STOCK PORTFOLIO TRACKER\\n")
    file.write(f"Total Investment = {total_investment}")

print("Result saved in result.txt")