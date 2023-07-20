filenames = ['document', 'report', 'presentation']
# Copy-paste the above list in a .py file and extend the code, so it prints out the output below:

for index, i in enumerate(filenames, 1):
    print(f'{index}-{i.capitalize()}.txt')

#########################################################
ips = ['100.122.133.105', '100.122.133.111']
# Copy-paste the ips list in a .py file and extend the program so it:
# 1. Prompts the user to input an index (e.g, 0 or 1).
# 2. Returns the IP address that has that index.
# Here is how the program would behave when executed:
chose_ip = int(input('Enter the index of the IP you want: '))
print(f'You chose {ips[chose_ip]}')


