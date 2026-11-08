# Module 3, Problem 4

# Define main() function 
def main(): 

	# Prompt user to enter make of car (e.g. Toyota)
	make = input("Enter make of car: ")

	# Prompt user to enter model of car (e.g. Rav4)
	model = input("Enter model of car: ")

	# Prompt user to enter msrp of car
	msrp = float(input("Enter MSRP of car: $"))

	# Prompt user to enter discounted percent 
	discount_percent = float(input("Enter the discount percent: "))

	# Calculate amount off msrp 
	amount_off = msrp * discount_percent

	# Calculate discounted price 
	discounted_price = msrp - amount_off

	# Display output back to user
	print("Make: " + make)
	print("Model: " + model)
	print(f"MSRP: ${msrp:.2f}")
	print(f"Discount Percent: ${discount_percent:.2f}")
	print(f"Amount Off: ${amount_off:.2f}")
	print(f"Discounted Price: ${discounted_price:.2f}")

# Call main() function
if __name__ == "__main__":
	main()