"""
Potential Optimization:
Define calculation variables (lines 19-29) outside the while loop and only update them when one of their components are changed.

Note to Instructor:
To determine the break-even point, I opted to use algebra instead of a loop, because I can get the exact answer in much less time while using less of the computer's memory. Then I can plug the result back in to the selling price and get a profit/loss of exactly $0.00
"""

# Define starting variable values
serving_cost = 1.00
labor_rate = 7.50
shop_rental = 800
utilities = 150
advertising = 100
selling_price = 4.00
servings_per_month = 1000

while True:
    # Define calculation variables
    # 8 hrs/day, 6 days/wk, 4 wks/month
    monthly_wage = (((labor_rate*8)*6)*4)
    # Total income = selling price * total servings
    total_income = selling_price * servings_per_month
    # Total expenses = total cost of servings + expenses + monthly wage for one employee
    total_expenses = (serving_cost * servings_per_month) + utilities + advertising + shop_rental + monthly_wage
    # Net profit = (total income - total expenses) rounded to two decimal places
    profit_loss_calc = round((total_income - total_expenses), 2)
    # Net profit per serving = net profit / total servings
    profit_per_serving = profit_loss_calc/servings_per_month

    # Print out expenses section of interface
    print("")
    print("Expenses:")
    print("1. Cost per serving:", serving_cost)
    print("2. Labor rate per hour:", labor_rate)
    print("3. Shop rental per month:", shop_rental)
    print("4. Utilities per month:", utilities)
    print("5. Advertising budget per month:", advertising)
    print("")

    # Print out income section of interface
    print("Income:")
    print("6. Selling price (each):", selling_price)
    print("7. Servings sold per month:", servings_per_month)
    print("")

    # Print out analysis section of the interface
    print("Analysis:")
    print("8. Profit/Loss Calculation")
    print("9. Potential Expense/Income Variance")
    print("10. Find Break-Even")
    print("")

    # Prompt user for input to determine modifications to the interface
    selection = str(input("Enter Selection (0 to Exit): "))
    print("")

    # Create an exit case
    if selection == "0":
        # Print final output
        print("Expenses:")
        print("1. Cost per serving:", serving_cost)
        print("2. Labor rate per hour:", labor_rate)
        print("3. Shop rental per month:", shop_rental)
        print("4. Utilities per month:", utilities)
        print("5. Advertising budget per month:", advertising)
        print("")
        print("Income:")
        print("6. Selling price (each):", selling_price)
        print("7. Servings sold per month:", servings_per_month)
        print("")
        print("Analysis:")
        print("8. Profit/Loss Calculation Report")
        print("9. Potential Expense/Income Variance Report")
        print("10. Find Break-Even")
        print("")

        # Stop the main while loop
        break


    # Create a case to change the cost per serving
    elif selection == "1":
        # Prompt the user for input and store it in new_serving_cost to be verified as a valid input
        new_serving_cost = input("Enter cost per serving: ")

        # Define variables: 
        # i increases each time a character is verified to determine when the string is completely verified
        i = 0
        # decimal_count ensures that the user does not enter more than one decimal point into the input
        decimal_count = 0

        # Iterate through each character (char) of the input string
        for char in new_serving_cost:
            # Use to identify a problem character (if needed):
            # print(char)

            # Check if the current char is a numeral:
            if char.isnumeric():

                i += 1 # Adds 1 to i, which is the verification counter

                # If i reaches the end of the input string:  
                if i == len(new_serving_cost):
                    # modify serving_cost to the float value of the verified input string
                    serving_cost = float(new_serving_cost)
                
                # If i has not reached the end of the input string, continue verifying the input
                else:
                    continue
            
            # If the current char was not a numeral,
            # Check if the current char is a decimal point:
            elif char == ".":

                i += 1 # Adds 1 to i, which is the verification counter
                decimal_count += 1 # Adds 1 to decimal_count

                # If there is more than one decimal point in the input:
                if decimal_count > 1:

                    # Return an error message
                    print("-"*20)
                    print("ERROR: Invalid data type, please enter a value containing only numerals and up to one decimal point")
                    print("-"*20)

                    # Use an input statement to pause the program so the output can be easily read.
                    print("")
                    input("Press ENTER to continue.")
                    print("")

                    # Stop the for loop
                    break

                # If the input ends with a decimal point:
                if i == len(new_serving_cost):
                    
                    # Return an error message
                    print("-"*20)
                    print("ERROR: Invalid value, please end your input with a numeral")
                    print("-"*20)

                    # Use an input statement to pause the program so the output can be easily read.
                    print("")
                    input("Press ENTER to continue.")
                    print("")
                
                # Otherwise, continue verifying the input
                else:
                    continue
            
            # If the current char was not a numeral or the only decimal point:
            else:
                
                # Return an error message
                print("-"*20)
                print("ERROR: Invalid data type, please enter a value containing only numerals and up to one decimal point")
                print("-"*20)
                
                # Use an input statement to pause the program so the output can be easily read.
                print("")
                input("Press ENTER to continue.")
                print("")

                # Stop the for loop
                break


    # Create a case to change the labor rate per hour
    elif selection == "2":
        # Prompt the user for input and store it in new_labor_rate to be verified as a valid input
        new_labor_rate = input("Enter labor rate per hour: ")

        # Define variables: 
        # i increases each time a character is verified to determine when the string is completely verified
        i = 0
        # decimal_count ensures that the user does not enter more than one decimal point into the input
        decimal_count = 0

        # Iterate through each character (char) of the input string
        for char in new_labor_rate:
            # Use to identify a problem character (if needed):
            # print(char)

            # Check if the current char is a numeral:
            if char.isnumeric():

                i += 1 # Adds 1 to i, which is the verification counter

                # If i reaches the end of the input string:  
                if i == len(new_labor_rate):
                    # modify serving_cost to the float value of the verified input string
                    labor_rate = float(new_labor_rate)
                
                # If i has not reached the end of the input string, continue verifying the input
                else:
                    continue
            
            # If the current char was not a numeral,
            # Check if the current char is a decimal point:
            elif char == ".":

                i += 1 # Adds 1 to i, which is the verification counter
                decimal_count += 1 # Adds 1 to decimal_count

                # If there is more than one decimal point in the input:
                if decimal_count > 1:

                    # Return an error message
                    print("-"*20)
                    print("ERROR: Invalid data type, please enter a value containing only numerals and up to one decimal point")
                    print("-"*20)

                    # Use an input statement to pause the program so the output can be easily read.
                    print("")
                    input("Press ENTER to continue.")
                    print("")

                    # Stop the for loop
                    break
                
                # If the input ends with a decimal point:
                if i == len(new_labor_rate):
                    
                    # Return an error message
                    print("-"*20)
                    print("ERROR: Invalid value, please end your input with a numeral")
                    print("-"*20)
                
                # Otherwise, continue verifying the input
                else:
                    continue
            
            # If the current char was not a numeral or the only decimal point:
            else:
                
                # Return an error message
                print("-"*20)
                print("ERROR: Invalid data type, please enter a value containing only numerals and up to one decimal point")
                print("-"*20)

                # Use an input statement to pause the program so the output can be easily read.
                print("")
                input("Press ENTER to continue.")
                print("")
                
                # Stop the for loop
                break

       
    # Create a case to change the shop rental per month
    elif selection == "3":
        # Prompt the user for input and store it in new_shop_rental to be verified as a valid input
        new_shop_rental = input("Enter shop rental per month: ")

        # Define variables: 
        # i increases each time a character is verified to determine when the string is completely verified
        i = 0

        # Iterate through each character (char) of the input string
        for char in new_shop_rental:
            # Use to identify a problem character (if needed):
            # print(char)

            # Check if the current char is a numeral:
            if char.isnumeric():

                i += 1 # Adds 1 to i, which is the verification counter

                # If i reaches the end of the input string:  
                if i == len(new_shop_rental):
                    # modify shop_rental to the float value of the verified input string
                    shop_rental = float(new_shop_rental)
                
                # If i has not reached the end of the input string, continue verifying the input
                else:
                    continue
            
            # If the current char was not a numeral:
            else:
                
                # Return an error message
                print("-"*20)
                print("ERROR: Invalid data type, please enter a value containing only numerals")
                print("-"*20)

                # Use an input statement to pause the program so the output can be easily read.
                print("")
                input("Press ENTER to continue.")
                print("")
                
                # Stop the for loop
                break


    # Create a case to change the utilities per month
    elif selection == "4":
        # Prompt the user for input and store it in new_utilities to be verified as a valid input
        new_utilities = input("Enter utilites per month: ")

        # Define variables: 
        # i increases each time a character is verified to determine when the string is completely verified
        i = 0

        # Iterate through each character (char) of the input string
        for char in new_utilities:
            # Use to identify a problem character (if needed):
            # print(char)

            # Check if the current char is a numeral:
            if char.isnumeric():

                i += 1 # Adds 1 to i, which is the verification counter

                # If i reaches the end of the input string:  
                if i == len(new_utilities):
                    # modify utilites to the float value of the verified input string
                    utilities = float(new_utilities)
                
                # If i has not reached the end of the input string, continue verifying the input
                else:
                    continue
            
            # If the current char was not a numeral:
            else:
                
                # Return an error message
                print("-"*20)
                print("ERROR: Invalid data type, please enter a value containing only numerals")
                print("-"*20)

                # Use an input statement to pause the program so the output can be easily read.
                print("")
                input("Press ENTER to continue.")
                print("")
                
                # Stop the for loop
                break


    # Create a case to change the advertising budget per month
    elif selection == "5":
        # Prompt the user for input and store it in new_advertising to be verified as a valid input
        new_advertising = input("Enter advertising budget per month: ")

        # Define variables: 
        # i increases each time a character is verified to determine when the string is completely verified
        i = 0

        # Iterate through each character (char) of the input string
        for char in new_advertising:
            # Use to identify a problem character (if needed):
            # print(char)

            # Check if the current char is a numeral:
            if char.isnumeric():

                i += 1 # Adds 1 to i, which is the verification counter

                # If i reaches the end of the input string:  
                if i == len(new_advertising):
                    # modify utilites to the float value of the verified input string
                    advertising = float(new_advertising)
                
                # If i has not reached the end of the input string, continue verifying the input
                else:
                    continue
            
            # If the current char was not a numeral:
            else:
                
                # Return an error message
                print("-"*20)
                print("ERROR: Invalid data type, please enter a value containing only numerals")
                print("-"*20)
                
                # Use an input statement to pause the program so the output can be easily read.
                print("")
                input("Press ENTER to continue.")
                print("")

                # Stop the for loop
                break


    # Create a case to change the selling price
    elif selection == "6":
        # Prompt the user for input and store it in new_selling_price to be verified as a valid input
        new_selling_price = input("Enter selling price: ")

        # Define variables: 
        # i increases each time a character is verified to determine when the string is completely verified
        i = 0
        # decimal_count ensures that the user does not enter more than one decimal point into the input
        decimal_count = 0

        # Iterate through each character (char) of the input string
        for char in new_selling_price:
            # Use to identify a problem character (if needed):
            # print(char)

            # Check if the current char is a numeral:
            if char.isnumeric():

                i += 1 # Adds 1 to i, which is the verification counter

                # If i reaches the end of the input string:  
                if i == len(new_selling_price):
                    # modify serving_cost to the float value of the verified input string
                    selling_price = float(new_selling_price)
                
                # If i has not reached the end of the input string, continue verifying the input
                else:
                    continue
            
            # If the current char was not a numeral,
            # Check if the current char is a decimal point:
            elif char == ".":

                i += 1 # Adds 1 to i, which is the verification counter
                decimal_count += 1 # Adds 1 to decimal_count

                # If there is more than one decimal point in the input:
                if decimal_count > 1:

                    # Return an error message
                    print("-"*20)
                    print("ERROR: Invalid data type, please enter a value containing only numerals and up to one decimal point")
                    print("-"*20)

                    # Use an input statement to pause the program so the output can be easily read.
                    print("")
                    input("Press ENTER to continue.")
                    print("")

                    # Stop the for loop
                    break

                # If the input ends with a decimal point:
                if i == len(new_selling_price):
                    
                    # Return an error message
                    print("-"*20)
                    print("ERROR: Invalid value, please end your input with a numeral")
                    print("-"*20)
                
                # Otherwise, continue verifying the input
                else:
                    continue
            
            # If the current char was not a numeral or the only decimal point:
            else:
                
                # Return an error message
                print("-"*20)
                print("ERROR: Invalid data type, please enter a value containing only numerals and up to one decimal point")
                print("-"*20)
                
                # Use an input statement to pause the program so the output can be easily read.
                print("")
                input("Press ENTER to continue.")
                print("")

                # Stop the for loop
                break


    # Create a case to change the total servings sold per month
    elif selection == "7":
        # Prompt the user for input and store it in new_servings_per_month to be verified as a valid input
        new_servings_per_month = input("Enter selling price: ")

        # Define variables: 
        # i increases each time a character is verified to determine when the string is completely verified
        i = 0
        # decimal_count ensures that the user does not enter more than one decimal point into the input
        decimal_count = 0

        # Iterate through each character (char) of the input string
        for char in new_servings_per_month:
            # Use to identify a problem character (if needed):
            # print(char)

            # Check if the current char is a numeral:
            if char.isnumeric():

                i += 1 # Adds 1 to i, which is the verification counter

                # If i reaches the end of the input string:  
                if i == len(new_servings_per_month):
                    # modify serving_cost to the float value of the verified input string
                    servings_per_month = float(new_servings_per_month)
                
                # If i has not reached the end of the input string, continue verifying the input
                else:
                    continue
            
            # If the current char was not a numeral,
            # Check if the current char is a decimal point:
            elif char == ".":

                i += 1 # Adds 1 to i, which is the verification counter
                decimal_count += 1 # Adds 1 to decimal_count

                # If there is more than one decimal point in the input:
                if decimal_count > 1:

                    # Return an error message
                    print("-"*20)
                    print("ERROR: Invalid data type, please enter a value containing only numerals and up to one decimal point")
                    print("-"*20)

                    # Use an input statement to pause the program so the output can be easily read.
                    print("")
                    input("Press ENTER to continue.")
                    print("")

                    # Stop the for loop
                    break

                # If the input ends with a decimal point:
                if i == len(new_servings_per_month):
                    
                    # Return an error message
                    print("-"*20)
                    print("ERROR: Invalid value, please end your input with a numeral")
                    print("-"*20)
                
                # Otherwise, continue verifying the input
                else:
                    continue
            
            # If the current char was not a numeral or the only decimal point:
            else:
                
                # Return an error message
                print("-"*20)
                print("ERROR: Invalid data type, please enter a value containing only numerals and up to one decimal point")
                print("-"*20)

                # Use an input statement to pause the program so the output can be easily read.
                print("")
                input("Press ENTER to continue.")
                print("")
                
                # Stop the for loop
                break


    # Create a case to report more details on the profit/loss calculation
    elif selection == "8":
        # Print out the results of the Monthly Profit/Loss Calculation
        print("+"*20)
        print(f"The Ice Cream Shop will have a monthly profit of ${profit_loss_calc} or the equivalent of ${profit_per_serving} per serving.")
        print("+"*20)

        """
        # Use an input statement to pause the program so the output can be easily read.
        print("")
        input("Press ENTER to continue.")
        print("")
        """


    # Create a case to generate a variance report for both expenses and income totals
    elif selection == "9":
        # Section Header:
        print("")
        print("Varying the Expenses From -10% to +10%:")

        # Iterate through percentage variations on the total expenses to determine possible expense totals and profit/loss calculations
        # Create a for loop where the iterable is i and the range is -10 to 10 (inclusive) by steps of two
        for i in range(-10, 11, 2):
            # Calculate the variance of the current iteration to use for calculations
            variance = i * 0.01
            # Calculate the variant total expense of the current iteration
            varied_total_expenses = total_expenses + (total_expenses * variance)
            # Calculate the variant profit/loss of the current iteration
            varied_profit_loss_calc = round((total_income - varied_total_expenses), 2)
            # Print the results to the terminal
            print("Percent: "+str(i)+" Expenses: "+str(varied_total_expenses)+" Profit/Loss: "+str(varied_profit_loss_calc))

        # Section Header:
        print("")
        print("Varying the Income From -10% to +10%:")

        # Iterate through percentage variations on the total income to determine possible income totals and profit/loss calculations
        # Create a for loop where the iterable is i and the range is -10 to 10 (inclusive) by steps of two
        for i in range(-10, 11, 2):
            # Calculate the variance of the current iteration to use for calculations
            variance = i * 0.01
            # Calculate the variant total income of the current iteration
            varied_total_income = total_income + (total_income * variance)
            # Calculate the variant profit/loss of the current iteration
            varied_profit_loss_calc = round((varied_total_income - total_expenses), 2)
            print("Percent: "+str(i)+" Income: "+str(varied_total_income)+" Profit/Loss: "+str(varied_profit_loss_calc))

        """
        # Use an input statement to pause the program so the output can be easily read.
        print("")
        input("Press ENTER to continue.")
        print("")
        """

    # Create a case to find the "break-even" point (the serving cost that sets the total profit/loss to zero)
    elif selection == "10":
        """
            # Break-even point: Total income - Total expenses = 0
            # Total income = (Total servings * Selling price)
            # 
            # -> Total income - Total expenses = 0
            # –> Total income = Total expenses
            # -> (Total servings * Selling price) = Total expenses
            # -> Selling Price = Total expenses/Total servings
        """
        # Calculate the break-even point and print the result
        break_even = total_expenses/servings_per_month
        print("+"*20)
        print(f"Break-Even occurs with a selling price of: {break_even}")
        print("+"*20)
        # Use an input statement to pause the program so the output can be easily read.
        print("")
        input("Press ENTER to continue.")
        print("")

    
    # Create a catch-all case to ensure that only valid selections are accepted
    else:
        # Return an error message
        print("-"*20)
        print("ERROR: Invalid selection, please choose a whole number from 0-10")
        print("-"*20)

        # Use an input statement to pause the program so the output can be easily read.
        print("")
        input("Press ENTER to continue.")
        print("")
