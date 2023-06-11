feet_inches = input('Enter feet and inches: ')

def convert(feetInch):
    raw_val = feetInch.split()
    feet = float(raw_val[0])
    inches = float(raw_val[1])
    meters = round(((feet * 0.3048) + (inches * 0.0254)),2)

    # return f"{feet}ft and {inches}in is equal to {meters} meters"
    # output of the string should be decoupled from other components, in this case we want to gain access the the meters value - retun one single value if you can
    return meters
    # ft and inches are now local variables so we can't access... look at decoupling functions 

result = convert(feet_inches)

if result < 1:
    print('Kid is too small for the slide.')
else:
    print('Kid can use the slide.')