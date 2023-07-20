#Create a program that prompts the user to input their name once. Then, the program prints out the name once with the first letter capitalized.
user_name = input("Please enter your name: ").capitalize()
print(user_name)

#Create a program that prompts the user to input their name once. Then, the program prints out the name once with the first letter capitalized.
user_name2 = input("Please enter your name: ")
pain_limit = 1

while pain_limit <= 10:
    print(user_name2.capitalize())
    pain_limit += 1

#Create a program that prompts the user to input their name repeatedly. Then, the program repeatedly prints out the name with the first letter capitalized.
user_name3 = input("Please enter your name: ")
pain_limit = 1

while pain_limit <= 10:
    print(user_name3.capitalize())
    pain_limit += 1
    user_name3 = input("Please enter your name: ")