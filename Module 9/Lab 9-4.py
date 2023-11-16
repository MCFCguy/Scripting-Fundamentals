# Write your class here
class DivisionByZeroError(Exception):
    def __init__(self):
        self.message = "Dividing a number by zero returns an undefined output."
# Test you custom exception class below
try:
    raise DivisionByZeroError
except DivisionByZeroError as e:
    print(e.message)
