# Create a function that converts liters to cubic meters knowing that 1000 liters make 1 cubic meter. 
def liters_to_metres(litres):
    cubic_meters = litres / 1000
    return cubic_meters

cubic_meters = liters_to_metres(13085)
print(round(cubic_meters, 2))

# Create a script that asks the user to enter a password. Then create a function that checks the strength of the user password. The function should return Strong Password if all of the following conditions are true:
# Eight or more characters
# At least one uppercase letter.
# At least one digit.
# Here is what happens when the user provides a password that satisfies all three conditions:
# Enter new password: | Strong Password | Weak Password 

def password_strength(password):
    if len(password) >= 8 and any(char.isdigit for char in password) and any(char.isupper() for char in password):
        return "Strong Password"
    else:
        return "Weak Password"
    
user_password =input("Enter a new Password: ")
print(password_strength(user_password))

# any() function returns True if at least one element of an iterable is true, if nopt any() returns false. 