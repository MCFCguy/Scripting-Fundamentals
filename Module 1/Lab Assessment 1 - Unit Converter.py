"""
This Program will convert units of weight and volume into other units of weight based on user input.
"""

def convert_kg(value):
	# Create variables for pounds and ounces and store their converted values
    pounds = value*2.20462
    ounces = value*35.274

    # Print the converted values to the console
    print(value, "kg converted is", pounds, "pounds and", ounces, "ounces.")

def convert_pounds(value):
	# Create variables for kilograms and ounces and store their converted values
    kilograms = value*0.453592
    ounces = value*16

    # Print the converted values to the console
    print(value , "pounds converted is" , kilograms , "kg and" , ounces , "ounces.")

def convert_ounces(value):
	# Create variables for kilograms and pounds and store their converted values
    kilograms = value*0.0283
    pounds = value*0.0625

    # Print the converted values to the console
    print(value , "ounces converted is" , kilograms , "kg and" , pounds , "pounds.")

def convert_fl_oz(value):
	# Create variables for litres, pints, and quarts and store their converted values
    litres = value*0.03
    pints = value*0.063
    quarts = value*0.031

    # Print the converted values to the console
    print(value, "fluid ounces converted is", litres, "litres,", pints, "pints, or", quarts, "quarts.")

def convert_litres(value):
	# Create variables for fluid ounces, pints, and quarts and store their converted values
    fl_oz = value*33.814
    pints = value*2.113
    quarts = value*1.057

    # Print the converted values to the console
    print(value, "litres converted is", fl_oz, "fluid ounces,", pints, "pints, or", quarts, "quarts.")

def convert_pints(value):
	# Create variables for litres, fluid ounces, and quarts and store their converted values
    litres = value*0.473
    fl_oz = value*16
    quarts = value*0.5

    # Print the converted values to the console
    print(value, "pints converted is", litres, "litres,", fl_oz, "fluid ounces, or", quarts, "quarts.")

def convert_quarts(value):
	# Create variables for litres, pints, and fluid ounces and store their converted values
    litres = value*0.946
    pints = value*2
    fl_oz = value*32

    # Print the converted values to the console
    print(value, "quarts converted is", litres, "litres,", pints, "pints, or", fl_oz, "fluid ounces.")

if __name__ == "__main__":
	# Test your code here\

    # Prompt user for input and store the result
    print("Enter a whole number to complete its unit conversion table:")
    number = input()

    # Print out weight results defined by the conversion functions.
    print("="*20)
    print("Weight Conversions:")
    print("="*20)

    convert_kg(int(number))
    print("-"*20)
    convert_pounds(int(number))
    print("-"*20)
    convert_ounces(int(number))

    # Print out volume results defined by the conversion functions.
    print("="*20)
    print("Volume Conversions:")
    print("="*20)

    convert_fl_oz(int(number))
    print("-"*20)
    convert_litres(int(number))
    print("-"*20)
    convert_pints(int(number))
    print("-"*20)
    convert_quarts(int(number))
    print("="*20)
