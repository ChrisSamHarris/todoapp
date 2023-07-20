# Define a function that has two parameters, year_of_birth and current_year . The current_year parameter should be a default parameter with the current year as a default value.
# The function should calculate and return the age of the user given the year of birth and the current year.
import datetime

currentYear = datetime.datetime.now().year

def user_age(year_of_birth, current_year=currentYear):
    age = currentYear - year_of_birth
    return age

print(user_age(1995))


# Your task for this exercise is to use the function you created in exercise 1. Then, below the function definition, get the year of birth from the user using an input function and 
# then call and print the defined function to get the user's age as output. 


user_inputted_age = int(input('What is your year of birth? '))
age_calc = user_age(user_inputted_age)
print(age_calc)

if age_calc > 120:
    print("wow you're old!")

# Write a program that gets a list of names from the user and returns the number of names given. You are encouraged to use a function. 

user_names = input('Give me a list of names... ')

def num_of_names(namesList): 
    name_list = user_names.split()
    totalnum = len(name_list)
    return totalnum

print(num_of_names(user_names))