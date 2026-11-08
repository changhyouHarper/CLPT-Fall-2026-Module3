# Module 3, Problem 3

# Define main() function 
def main():

	# Prompt the user to enter an amount 
	total_amount = int(input("Enter an amount: $"))

	# Calculate individual amount 
	individual_amount = total_amount / 3

	# Display output back to user 
	print(f"Amount Per Individual: ${individual_amount:.2f}")

# Call main() function
if __name__ == "__main__":
	main()