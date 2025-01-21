# Kris Lee, 2/19/2024
import random

rand_num = random.randint(0, 50)                # generates and chooses a random number from 0-50.
random_list = [num for num in range(rand_num)]  # from chosen random number. Using list comprehension to a create a list from 0 to given range.
random.shuffle(random_list)                     # shuffles the list to a random sequence.

print(f"\nUnsorted List: {random_list}\n")

while random_list != sorted(random_list):       # keeps checking until the list is completely sorted. Compares unsorted with sorted list.
    
    for index in range(len(random_list) - 1 ):  # stops prematurely to remove index error.
        
        if random_list[index] > random_list[index + 1]: # if the value on the left is greater than the one on the right, it needs swapped. 
            random_list[index], random_list[index + 1] = random_list[index + 1], random_list[index] # swapping elements
            
print(f"\nSorted List: {random_list}\n")