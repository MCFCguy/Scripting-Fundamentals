name = input("Enter your name: ")
correct_password = "Pas$Word"
condition = True

while condition:
    password = input("Enter your password: ")
    if password == correct_password:
        print("Welcome back, " + name)
        break
    else:
        print("Incorrect password, try again...")
