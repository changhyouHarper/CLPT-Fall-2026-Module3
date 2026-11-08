# Module 3, Problem 5

# Define main() function
def main(): 

	# Prompt the user to enter the radius of circle 
	radius = float(input("Enter radius of circle: "))

	# Calculate area of the circle 
	area = 3.14 * (radius * radius)

	# Calculate perimeter of the circle 
	perimeter = 2 * 3.14 * radius 

	# Display area and perimter back to user 
	print(f"Circle Area: {area:.2f}")
	print(f"Circle Perimeter: {perimeter:.2f}")

# Call main() function
if __name__ == "__main__":
	main()