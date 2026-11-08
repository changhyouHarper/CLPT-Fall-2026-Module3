# Module 3, Problem 2

# Define main() function
def main():

	# Prompt user to enter last name
	last_name = input("Enter last name: ")

	# Prompt user to enter midterm grade
	midterm_grade = int(input("Enter midterm grade: "))

	# Prompt user to enter final exam grade
	final_grade = int(input("Enter final grade: "))

	# Calculate 40% of midterm grade 
	midterm_score = midterm_grade * 0.40

	# Calculate 60% of final exam grade 
	final_score = final_grade * 0.60

	# Calculate total exam points 
	total_exam_points = midterm_score + final_score

	# Display output back to user
	print("Last Name: " + last_name)
	print(f"Total Exam Points: {total_exam_points:.2f}")

# Call main() function
if __name__ == "__main__":
	main()