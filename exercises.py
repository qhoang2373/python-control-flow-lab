# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

# def check_letter():
#     # Your control flow logic goes here
#     letter = input("Enter a letter (a-z or A-Z): ")

#     if len(letter) == 1 and letter.isalpha():
#         letter = letter.lower()
    
#     if letter in "aeiou":
#         print(f"The letter '{letter}' is a vowel.")
#     elif letter.isalpha():
#         print(f"The letter '{letter}' is a consonant." )
#     else:
#         print("Invalid input")

# # Call the function
# check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

# def check_voting_eligibility():
#     # Your control flow logic goes here
#     voting_age = 18

#     try:
#         age = int(input("Please enter your age: "))

#         if age < 0:
#             print("Invalid age.")
#         elif age >= voting_age:
#             print("You are eligible to vote!")
#         else:
#             print("You are not old enough to vote.")

#     except ValueError:
#         print("Invalid input.")

# # Call the function
# check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

# def calculate_dog_years():
#     try:
#         # Prompt the user to enter the dog's age
#         dog_age = int(input("Input the dog's age: "))

#         # Check if the age is valid (non-negative)
#         if dog_age < 0:
#             print("Invalid age.")
#         else:
#             # Calculate dog years
#             if dog_age <= 2:
#                 dog_years = dog_age * 10
#             else:
#                 dog_years = 2 * 10 + (dog_age - 2) * 7

#             # Print the result
#             print(f"The dog's age in dog years is {dog_years}.")
#     except ValueError:
#         print("Invalid input.")

# # Call the function
# calculate_dog_years()

# def weather_advice():
#     # Ask if it is cold
#     is_cold = input("Is it cold? (yes/no): ").strip().lower()

#     # Ask if it is raining
#     is_raining = input("Is it raining? (yes/no): ").strip().lower()

#     # Determine clothing advice based on the inputs
#     if is_cold == 'yes' and is_raining == 'yes':
#         print("Wear a waterproof coat.")
#     elif is_cold == 'yes' and is_raining == 'no':
#         print("Wear a warm coat.")
#     elif is_cold == 'no' and is_raining == 'yes':
#         print("Carry an umbrella.")
#     elif is_cold == 'no' and is_raining == 'no':
#         print("Wear light clothing.")
#     else:
#         print("Invalid input. Please enter 'yes' or 'no'.")

# # Call the function
# weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Prompt user for month and day input
    month = input("Enter the month of the year (Jan - Dec): ").strip().capitalize()
    try:

        day = int(input("Enter the day of the month: ").strip())

        # Validate the month and day
        if month not in {'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'}:
            print("Invalid month. Please enter a valid month (e.g., Jan, Feb, etc.).")
            return

        if day < 1 or day > 31:
            print("Invalid day. Please enter a day between 1 and 31.")
            return

        # Determine the season
        if (month == 'Dec' and day >= 21) or month in {'Jan', 'Feb'} or (month == 'Mar' and day <= 19):
            season = 'Winter'
        elif (month == 'Mar' and day >= 20) or month in {'Apr', 'May'} or (month == 'Jun' and day <= 20):
            season = 'Spring'
        elif (month == 'Jun' and day >= 21) or month in {'Jul', 'Aug'} or (month == 'Sep' and day <= 21):
            season = 'Summer'
        elif (month == 'Sep' and day >= 22) or month in {'Oct', 'Nov'} or (month == 'Dec' and day <= 20):
            season = 'Fall'
        else:
            print("Invalid date. Please enter a date for the specified month.")
            return

        # Print the result
        print(f"{month} {day} is in {season}.")

    except ValueError:
        print("Invalid input.")

# Call the function
determine_season()
