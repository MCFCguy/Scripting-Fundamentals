miles = 60
hours = 3

knots = miles/1.15078
feet = miles*5280
seconds = hours*3600

speed_in_knots = knots/hours
speed_in_mph = miles/hours
speed_in_fps = feet/seconds

print("The speed in knots is:", speed_in_knots)
print("The speed in miles per hour is", speed_in_mph)
print("The speed in feet per second is", speed_in_fps)
