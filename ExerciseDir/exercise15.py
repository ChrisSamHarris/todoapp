# Your task is to create a program that generates a random whole number. 
# As you can see, the program first asks the user to enter a whole number. Then, once the user enters a number, the program asks the user again to enter another number.
# Then, the program returns a random number that falls between the two whole numbers. 
# Enter the lower bound: 12
# Enter the upper bound: 15 
import random
low_num = int(input('Enter the lower bound: ').strip()) + 1
high_num = int(input('Enter the higher bound: ').strip()) - 1

print(random.randint(low_num, high_num))

# Python 3 Module Index = https://docs.python.org/3/py-modindex.html