# Create a program that:
# 1. Prompts the user to input a (dollar) amount.
# 2. Calculates the corresponding amount in euros, given an exchange rate of 0.95.
# 3. Prints out the amount in euros, as shown in the screenshot below.

dollars = input("How many dollars have you got? $")
print(f'The amount in euros is: \n{int(dollars) * 0.95}')

# The list below represents the ranking of three athletes. John won 1st place, Sen got 2nd, and Lisa the 3rd.
# Create a program that:
# 1. Contains the above list.
# 2. Prompts the user to input a rank number.
# 3. Returns the person who has the given rank.

ranking = ['John', 'Sen', 'Lisa']
req_rank = input("Enter a rank number:")
print(f'{ranking[int(req_rank) - 1]}')

# We have the same list:
# This time you need to create a program that:
# 1. Contains the above list.
# 2 Prompts the user to input the person's name.
# 3. Returns the rank that person has.

ranking = ['John', 'Sen', 'Lisa']
race_num = input('Enter a name: ').capitalize().strip()

print(f'{ranking.index(race_num) + 1}')
# ranking.index(race_num) = returns an int ^^ 
