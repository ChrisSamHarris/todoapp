import bonus14_functions as funk

feet_inches = input('Enter feet and inches: ')

feet, inches = funk.parse(feet_inches)
meters = funk.convert(feet, inches)

print(f"Feet: {feet}")
print(f"Inches: {inches}")
print(f"{feet}ft{inches}in is equal to {meters} meters")

if meters < 1:
    print('Kid is too small for the slide.')
else:
    print('Kid can use the slide.')