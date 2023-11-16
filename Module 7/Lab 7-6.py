class Bird:
    def __init__(self, wingspan, lifespan, speed):
        self.wingspan = wingspan
        self.lifespan_in_years = lifespan
        self.speed_in_mph = speed

    def __str__(self):
        return f"The {type(self).__name__.lower()} "\
            f"has a wingspan up to {self.wingspan}ft,"\
            f" has a lifespan of {self.lifespan_in_years} years and "\
            f"can fly at a maximum speed of {self.speed_in_mph}mph."

# Write your Eagle class here
class Eagle(Bird):

    def __init__(self, wingspan, lifespan, speed):
        clutch_size = 3
        self.clutch_size = clutch_size
        super().__init__(wingspan, lifespan, speed)

    def __str__(self):
        return f"The {type(self).__name__.lower()} "\
            f"has a wingspan up to {self.wingspan}ft,"\
            f" has a lifespan of {self.lifespan_in_years} years and "\
            f"can fly at a maximum speed of {self.speed_in_mph}mph."\
            f"It also has a clutch size up to {self.clutch_size}."


# This code is used to test your class
if __name__ == '__main__':
    eagle = Eagle(7.5, 20, 99)
    print(eagle)
