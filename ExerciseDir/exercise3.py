# Create a program that does the following:
# 1. Prompts the user to input the country they are from.
# f the user enters the word USA, the program prints out Hello.
# 3. If the user enters the word  India, the program prints out Namaste.
# 4. If the user enters the word Germany, the program prints out Hallo.

user_country = input("What country are you from? ").capitalize().strip()

# if user_country == "Usa":
#     print('Hello')
# if user_country == "India":
#     print('Namaste')
# if user_country == "Germany":
#     print('Hallo')

match user_country:
    case 'Usa':
        print('Hello')
    case 'India':
        print('Namaste')
    case 'Germany':
        print('Hallo')


##### Exercise 2 ######
print('\n ##### Ex 2 ######\n')
# ingredients = ["john smith", "sen plakay", "dora ngacely"]
# Copy-paste the above line into your IDE and write a for-loop below that line that makes the program produce the names in title:
ingredients = ["john smith", "sen plakay", "dora ngacely"]

for i in ingredients:
    print(i.title())

