# Write your Package class here
class Package:
    item_limit = 6

    def __init__(self, items):
        self.items = items
        if self.items > Package.item_limit and type(self.items) == int :
            print(f"The maximum item limit has been exceeded. {self.items - Package.item_limit} items must be removed from the package.")
        elif self.items < 1 or type(self.items) != int:
            print("Please insert a valid number of items.")
        else:
            print(f"There are {self.items} packages being shipped out.")

# This is to test your code
if __name__ == '__main__':
    morepackages = True
    while morepackages:
        items = int(input("How many items are in the package?: "))
        package = Package(items)
        yn = input('Ship more packages? Y/N ')
        morepackages = yn == 'y' or yn == 'Y'
