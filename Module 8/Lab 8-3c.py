import random
# Write your function here
def number_randomizer(num):
    output_list = []
    for i in range(0, num):
        output_list.append(random.randint(0, 100))
    return output_list

print(number_randomizer(2)) 
print(number_randomizer(4))
print(number_randomizer(6))
