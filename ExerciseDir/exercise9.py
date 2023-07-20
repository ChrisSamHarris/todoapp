# Write a program that asks users to enter a password. Then, it checks if the password length is greater than 7 and returns "Great password there!".
# If the password has 7 or fewer characters, the program returns, "Your password is weak".
user_password = input('Enter a new password: ')

if len(user_password) > 7:
    print('Great password there!')
else:
    print('Your password is weak.')



# Extend the program we built in Coding Exercise 1 by adding a new feature. The new feature should allow the program to return "Password is OK, but not too strong" when the password is exactly seven characters long.
if len(user_password) == 7:
    print("Password is OK, but not too strong")
elif len(user_password) > 7:
    print('Great password there!')
else:
    print('Your password is weak.')