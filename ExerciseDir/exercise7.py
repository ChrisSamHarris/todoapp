# Extend the code below so the code capitalizes all the names and the surnames of the list and then prints the new list.
names = ["john smith", "jay santi", "eva kuki"]
names = [i.title() for i in names]
print(names)

# Extend the code below so the code prints out a list containing the number of characters for each username.
usernames = ["john 1990", "alberta1970", "magnola2000"]
username_len = [len(i) for i in usernames]
print(username_len)

# Extend the code below so the code prints out a list containing the same items as floats.
user_entries = ['10', '19.1', '20']
float_entries = [float(i) for i in user_entries]
print(float_entries)

# Extend the code below so the code prints out the sum of the numbers.
user_entries = ['10', '19.1', '20']
sum_entries = [float(num) for num in user_entries]
print(sum(sum_entries))