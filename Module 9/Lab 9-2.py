# Use the function return to create an error
def createError():
    # Task 1
    # Write your code here
    dinning = dict(name = "Johnny's Restaurant", location = "Times Square")
    print(dinning["address"])

    # Task 2
    # Write you import modules here
    import string
    return string.asciiletters

# Use this code to test your function
if __name__ == '__main__':
    createError()
