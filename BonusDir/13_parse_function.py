multiline_string = """
much more practical
way of
multi-line strings
"""


feet_inches = input('Enter feet and inches: ')

# decoupling = creating two different functions to segment capabilities - Think of a cafe: Barista & Cashier 
def parse(feetInch):
    raw_val = feetInch.split()
    feet = float(raw_val[0])
    inches = float(raw_val[1])
    return feet, inches
    # return {"feet": feet, "inches": inches}
    # call with parsed = parse(feet_inches) then access values from the dict using "parsed['feet']"

feet, inches = parse(feet_inches)
print(f"Feet: {feet}")
print(f"Inches: {inches}")

def convert(feet, inches):
    meters = round(((feet * 0.3048) + (inches * 0.0254)),2)
    # return f"{feet}ft and {inches}in is equal to {meters} meters"
    # output of the string should be decoupled from other components, in this case we want to gain access the the meters value - retun one single value if you can
    return meters
    # OBSOLETE ft and inches are now local variables so we can't access... look at decoupling functions 

meters = convert(feet, inches)
print(f"{feet}ft and {inches}in is equal to {meters} meters")

if meters < 1:
    print('Kid is too small for the slide.')
else:
    print('Kid can use the slide.')