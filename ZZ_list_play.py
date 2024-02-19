import random

#created list
all_numbers = []

for item in range(0, 5):
    #generate a random number
    mystery_num = random.randint(1, 10)
    #put mystery_num item into list if it does not already exist in list
    if mystery_num not in all_numbers:
        all_numbers.append(mystery_num)

all_numbers.sort() #put items in list in order
print(all_numbers)