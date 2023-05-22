with open('../files/bonus9-doc.txt', 'r') as file:
    # print(file.read())
    # file.read()
    content = file.read()
    # Can not use 'file.read()' multiple times as the status is exhausted - can only be read ONCE during a file open - you will have to re-open to use multiple times
    # In order to call the file.read() function various times defin the value in a variable
    # once indented code block completes execution then the file is closed explcitly

print(content)

####### by default the open() function defines 'r' (read) as a default value - however should be inputted to ensure the code is readable #######
# with open('../files/doc.txt') as file:
#     print(file.read())
#    

date = input("Enter today's date: ")
mood = input('How would you rate your mood today from 1-10? ')
thoughts = input('Let your thoughts flow:\n')

with open(f'./journal/{date}.txt', 'w') as file:
    file.write(f'Todays Rating: {mood}' + 2*'\n')
    file.write(f'{thoughts}')
