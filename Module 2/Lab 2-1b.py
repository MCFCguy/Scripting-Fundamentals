# Prompt the user to input a whole number of days that they have had a driver's license
print("Days you have been driving:")

# Store the input as an integer
drivingfor = int(input())

# Define the formulas dividing the time into years + weeks + days.
years = int(drivingfor//365)
weeks = int((drivingfor%365)/7)
days = int(drivingfor - (years*365) - (weeks*7))

# Print the results of the calculation based on the user input
print("You have been driving for:")
print("Years:", years)
print("Weeks:", weeks)
print("Days:", days)
