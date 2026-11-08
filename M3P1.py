# Module 3, Problem 1

# Define main() function 
def main():

	# Prompt the user to enter stock ticker symbol 
	stock_symbol = input("Enter Stock Ticker Symbol: ")

	# Prompt the user to enter number of shares
	num_shares = float(input("Enter number of shares: "))

	# Prompt the user to enter cost per share
	cost_per_share = float(input("Enter cost per share: "))

	# Calculate amount invested and store in variable 
	amount_invested = num_shares * cost_per_share

	# Display output back to user
	print(f"Total Amount Invested: ${amount_invested:.2f}")

# Call main() function
if __name__ == "__main__":
	main()