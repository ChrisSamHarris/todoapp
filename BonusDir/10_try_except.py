# Logical issues = only Humans can spot 

# Scenario = Calculate the area of a rectangle 

try: 
    width = float(input('Enter rectangle width: '))
    length = float(input('Enter rectangle length: '))

    if width == length:
        exit('This is a square. Both the width and length are the same value.')

    area = width * length
    print(area)

except ValueError: 
    print('Please enter a numerical value (1,2,3,4 etc).')
    # continue not required as we are not in a while loop